# Network and Port Operations
#Script: Check if a Port is Open
=================================

import socket

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)  # Timeout after 5 seconds
        try:
            s.connect((host, port))
            print(f"Port {port} on {host} is open.")
        except (socket.timeout, ConnectionRefusedError):
            print(f"Port {port} on {host} is closed.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
check_port("google.com", 80)  # Check if port 80 (HTTP) is open on google.com
