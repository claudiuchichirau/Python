import os
import sys

def rename_files(directory):
    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return
    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")
        return

    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print(f"No files found in directory '{directory}'.")
        return

    try:
        for i, file_name in enumerate(files, start=1):
            old_path = os.path.join(directory, file_name)
            new_name = f"file{i}.{file_name.split('.')[-1]}"
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
    else:
        directory_path = sys.argv[1]
        rename_files(directory_path)
