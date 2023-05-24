import os

def calculate_average_file_size(directory):
    total_size = 0
    file_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                total_size += file_size
                file_count += 1

    if file_count == 0:
        return 0

    average_size_mb = total_size / (file_count * 1024 * 1024)
    return average_size_mb

# Prompt the user to enter the directory path
directory_path = input("Enter the directory path: ")

# Call the function and print the average file size
average_size = calculate_average_file_size(directory_path)
print(f"Average file size in the directory: {average_size:.2f} MB")
