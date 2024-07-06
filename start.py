import subprocess
from subprocess import call
import struct
import sys
from time import sleep
from SX127x.LoRa import *
from SX127x.board_config import BOARD
# import the python libraries

taking_pic = False
counter = 0
#read image with a specified chunk size
CHUNK_SIZE = 200

output_path = 'webcam_image' + str(counter) + '.jpg'
subprocess.run(['ffmpeg', '-f', 'video4linux2', '-i', '/dev/video0','-vframes', '1', output_path], check=True)
print(f"Image saved as {output_path}")
f = open(f"{output_path}", 'rb')   
            
            

 #read the next chunk

    
BOARD.setup()
# is used to set the board and LoRa parameters
class LoRaBeacon(LoRa):

    def __init__(self, verbose=False):
        super(LoRaBeacon, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        # sleep to save power
        self.set_dio_mapping([1,0,0,0,0,0])
        #go to this web to read the doc: https://cdn-shop.adafruit.com/product-files/3179/sx1276_77_78_79.pdf
    def start(self):
        global args
        self.write_payload([])
        self.set_mode(MODE.TX)
        while True:
              sleep(1)
    def on_tx_done(self):
        global taking_pic
        global f
        global CHUNK_SIZE
        global counter
        global output_path
        
        self.set_mode(MODE.STDBY)
        self.clear_irq_flags(TxDone=1)
        sys.stdout.flush()
        if taking_pic:
            
            output_path = 'webcam_image' + str(counter) + '.jpg'
            subprocess.run([
                'ffmpeg', '-f', 'video4linux2', '-i', '/dev/video0',
                '-vframes', '1', output_path
            ], check=True)
            print(f"Image saved as {output_path}")
    
            #read image with a specified chunk size
            CHUNK_SIZE = 200
            f = open(output_path, 'rb')
            taking_pic = False
            self.set_mode(MODE.TX)
            
        else:
            chunk = bytearray(f.read(CHUNK_SIZE)) #read the next chunk
            numbers = list(chunk)
            sleep(0.15)
            if chunk:
                print(numbers)
                self.write_payload(numbers)
                self.set_mode(MODE.TX)
            else:
                payload = [999]
                print(payload)
                taking_pic = True
                counter = counter + 1
                self.write_payload(payload)
                self.set_mode(MODE.TX)
                


lora = LoRaBeacon(verbose=False)

lora.set_pa_config(pa_select=1)

assert(lora.get_agc_auto_on() == 1)

try: sleep(0.001)
except: pass

try:
    # Run the FFmpeg command to capture a single frame from the webcam
    
    
    lora.start()
except KeyboardInterrupt:
    sys.stdout.flush()
    sys.stderr.write("KeyboardInterrupt\n")
 #print the transmitted values on the console and terminate the program using a keyboard interrupt   
finally:
    sys.stdout.flush()
    lora.set_mode(MODE.SLEEP)
    BOARD.teardown()
