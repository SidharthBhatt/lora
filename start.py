import subprocess

def capture_image(output_path='output.jpg'):
    try:
        # Run the FFmpeg command to capture a single frame from the webcam
        subprocess.run([
            'ffmpeg', '-f', 'video4linux2', '-i', '/dev/video0',
            '-vframes', '1', output_path
        ], check=True)
        print(f"Image saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    capture_image('webcam_image.jpg')
