import subprocess
from subprocess import call
       
def capture_image(output_path='webcam_image.jpg'):
    
    # Run the FFmpeg command to capture a single frame from the webcam
    subprocess.run([
        'ffmpeg', '-f', 'video4linux2', '-i', '/dev/video0',
        '-vframes', '1', output_path
    ], check=True)
    print(f"Image saved as {output_path}")
    
    #open image as byte array
    with open("webcam_image.jpg", "rb") as image:
        f = image.read()
        b = bytearray(f)
        
        for i in range(0, len(b), 250):
            print(b[i:i + 250])
        print(b[0])
    
if __name__ == "__main__":
    capture_image('webcam_image.jpg')