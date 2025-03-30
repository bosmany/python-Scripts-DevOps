# Script: Calculate MD5 and SHA256 Hashes of a File 
===============
import hashlib

def calculate_file_hash(file_path, hash_type="md5"):
    try:
        hash_func = hashlib.md5() if hash_type == "md5" else hashlib.sha256()
        
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):  # Read the file in chunks of 8KB
                hash_func.update(chunk)
        
        print(f"{hash_type.upper()} Hash of '{file_path}': {hash_func.hexdigest()}")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
calculate_file_hash("example.txt", "md5")      # Replace 'example.txt' with your file path
calculate_file_hash("example.txt", "sha256")   # Replace 'example.txt' with your file path
