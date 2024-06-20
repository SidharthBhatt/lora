import subprocess
from subprocess import call
from time import sleep
import sys
from SX127x.LoRa import *
from SX127x.board_config import BOARD

# Setup the LoRa board
BOARD.setup()

class LoRaBeacon(LoRa):
    def __init__(self, verbose=False):
        super(LoRaBeacon, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([1, 0, 0, 0, 0, 0])

    def start(self):
        while True:
            try:
                # Capture and send image
                capture_image('webcam_image.jpg')
                split_image('webcam_image.jpg', chunk_size=250, prefix='index')
                send_image_chunks(self, 'index')
                sleep(10)  # Delay before capturing the next image
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    def on_tx_done(self):
        self.set_mode(MODE.STDBY)
        self.clear_irq_flags(TxDone=1)
        sys.stdout.flush()

def capture_image(output_path='webcam_image.jpg'):
    try:
        # Run the FFmpeg command to capture a single frame from the webcam
        subprocess.run([
            'ffmpeg', '-f', 'video4linux2', '-i', '/dev/video0',
            '-vframes', '1', output_path
        ], check=True)
        print(f"Image saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def split_image(input_path='webcam_image.jpg', chunk_size=250, prefix='index'):
    # Split the image into chunks
    try:
        call(f'split -b {chunk_size} {input_path} {prefix}', shell=True)
        print(f"Image split into pieces with prefix '{prefix}'")
    except Exception as e:
        print(f"An error occurred while splitting the image: {e}")

def send_image_chunks(lora, prefix):
    try:
        import glob
        chunk_files = sorted(glob.glob(f"{prefix}*"))
        for chunk_file in chunk_files:
            with open(chunk_file, 'rb') as file:
                data = file.read()
                lora.write_payload(list(data))
                lora.set_mode(MODE.TX)
                while lora.get_irq_flags()['tx_done'] == 0:
                    sleep(0.1)
                lora.clear_irq_flags(TxDone=1)
                print(f"Sent chunk: {chunk_file}")
    except Exception as e:
        print(f"An error occurred while sending the chunks: {e}")

# Main execution
if __name__ == "__main__":
    lora = LoRaBeacon(verbose=False)
    lora.set_pa_config(pa_select=1)
    assert(lora.get_agc_auto_on() == 1)

    try:
        lora.start()
    except KeyboardInterrupt:
        sys.stdout.flush()
        sys.stderr.write("KeyboardInterrupt\n")
    finally:
        sys.stdout.flush()
        lora.set_mode(MODE.SLEEP)
        BOARD.teardown()
