import os

def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Files and directories in '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
list_files(".")  # Lists files in the current directory
