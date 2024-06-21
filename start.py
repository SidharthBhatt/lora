import subprocess
from subprocess import call

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

def read_binary_file(file_path):
    # Read binary data from the file
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            print(data)
            return data
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def save_binary_file(data, output_path):
    # Save binary data to a file
    try:
        with open(output_path, 'wb') as file:
            file.write(data)
        print(f"Data saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    capture_image('webcam_image.jpg')
    split_image('webcam_image.jpg', chunk_size=250, prefix='index')

    # Read the content of the first split piece
    binary_data = read_binary_file('indexaa')

    if binary_data is not None:
        # Save the binary data to another file
        save_binary_file(binary_data, 'indexaa_copy')
