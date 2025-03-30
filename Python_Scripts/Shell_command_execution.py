# Shell Command Execution
# Script: Execute Shell Commands and Capture Output
=========================================================
import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode == 0:
            print("Command Output:")
            print(result.stdout)
        else:
            print("Command Error:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
execute_command("ls")  # Replace 'ls' with any shell command (e.g., 'dir' for Windows)
