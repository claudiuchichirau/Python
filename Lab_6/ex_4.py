import os
import sys

def count_files_by_extension(directory):
    try:
        extension_count = {}

        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                _, file_extension = os.path.splitext(file)
                extension = file_extension.lower()

                extension_count[extension] = extension_count.get(extension, 0) + 1

        print(f"File counts by extension in '{directory}':")
        for ext, count in extension_count.items():
            print(f"{ext}: {count} files")

    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
    else:
        directory_path = sys.argv[1]
        count_files_by_extension(directory_path)
