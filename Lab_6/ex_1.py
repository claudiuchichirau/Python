import os
import sys

def read_files_in_directory(directory, extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        directory = os.path.abspath(directory)

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a valid directory.")

        files = [file for file in os.listdir(directory) if file.endswith(extension)]

        if not files:
            raise FileNotFoundError(f"No files with extension '{extension}' found in '{directory}'.")

        for file in files:
            file_path = os.path.join(directory, file)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"Content of '{file}':\n{content}\n{'-'*50}")
            except Exception as file_read_error:
                print(f"Error reading file '{file}': {file_read_error}")

    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        read_files_in_directory(directory_path, file_extension)
