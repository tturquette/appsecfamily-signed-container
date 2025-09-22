import hashlib

def hash_password(password):
    # Using weak MD5 hash
    return hashlib.md5(password.encode()).hexdigest()
