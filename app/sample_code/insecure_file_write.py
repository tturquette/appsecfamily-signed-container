def write_config(filename, data):
    # Writing sensitive data to world-readable file
    with open(filename, "w") as f:
        f.write(data)
