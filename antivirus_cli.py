import os
import threading
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama

def scan_file(file_path):
    # Simulate scanning for a malicious file
    malicious_file = "malicious_file.exe"
    if os.path.basename(file_path) == malicious_file:
        return f"{Fore.RED}Found malicious file:{Style.RESET_ALL} {file_path}"
    else:
        return f"{Fore.GREEN}File is clean:{Style.RESET_ALL} {file_path}"

def scan_directory(directory):
    # Simulate scanning all files in a directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(scan_file(file_path))

def run_cli(directory):
    print(f"Scanning directory: {directory}")

    # Simulate multi-threading by scanning files in parallel
    scan_thread = threading.Thread(target=scan_directory, args=(directory,))
    scan_thread.start()

    # Wait for the scan thread to finish
    scan_thread.join()

    print("Scanning completed.")

if __name__ == "__main__":
    directory = input("Enter the directory to scan: ")
    run_cli(directory)
