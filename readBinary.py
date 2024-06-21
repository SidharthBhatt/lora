def read_binary_file(file_path):
    try:
	counter = 0
        with open(file_path, 'rb') as file:
            byte = file.read(1)
            while byte:
                # Print the byte in binary format
                print(format(ord(byte), '08b'), end=' ')
                byte = file.read(1)
		counter = counter + 1
		print(counter)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_binary_file('indexaa')
