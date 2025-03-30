#JSON/YAML Parsing
#Script: Parse JSON Files
=========================

import json

def parse_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            print("JSON Data:", data)
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except json.JSONDecodeError:
        print("Failed to decode JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
parse_json("config.json")  # Replace with your JSON file path

