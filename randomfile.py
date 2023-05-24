import os
import random
import string

def generate_random_text_file(directory):
    # Generate random file size between 16KB and 128KB
    file_size = random.randint(16, 128) * 1024  # Convert KB to bytes

    # Generate random file name
    file_name = ''.join(random.choices(string.ascii_lowercase, k=8))
    file_path = os.path.join(directory, file_name + '.txt')

    # Generate random content for the file
    content = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size))

    # Create the file and write the content
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"Generated file: {file_path}")

def generate_random_text_files(directory, num_files):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate random text files
    for _ in range(num_files):
        generate_random_text_file(directory)

# Prompt user for directory path and number of files
directory = input("Enter the directory path: ")
num_files = int(input("Enter the number of files to generate (up to 20): "))

# Limit the number of files to a maximum of 20
num_files = min(num_files, 20)

generate_random_text_files(directory, num_files)
