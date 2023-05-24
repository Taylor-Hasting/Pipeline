import os
import random
import string

def generate_random_text_file(directory, filename, file_size):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        content = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=file_size))
        file.write(content)

def generate_random_text_files(directory, num_files):
    for i in range(num_files):
        file_size = random.randint(16, 128) * 1024  # Convert to bytes
        filename = f"file_{i+1}.txt"
        generate_random_text_file(directory, filename, file_size)

# Prompt the user to enter the directory path
directory_path = input("Enter the directory path where you want to generate the files: ")

# Prompt the user to enter the number of files to generate (up to 20)
num_files = int(input("Enter the number of files to generate (up to 20): "))

# Generate random text files
if num_files > 20:
    num_files = 20

generate_random_text_files(directory_path, num_files)
print(f"{num_files} random text files have been generated in the directory: {directory_path}")
