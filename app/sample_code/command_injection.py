import os

def delete_file(filename):
    # Vulnerable to command injection
    os.system(f"rm {filename}")
