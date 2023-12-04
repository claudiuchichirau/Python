import os
import sys

def calculate_total_size(directory):
    try:
        total_size = 0

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)

        print(f"Total size of all files in '{directory}': {total_size} bytes")

    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
    else:
        directory_path = sys.argv[1]
        calculate_total_size(directory_path)
