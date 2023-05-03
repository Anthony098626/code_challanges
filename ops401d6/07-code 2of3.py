#!/user/bin/python3
import os
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and saves it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_directory(path, key):
    """
    Recursively encrypts a directory and all its contents
    """
    for root, _, files in os.walk(path):
        for file in files:
            with open(os.path.join(root, file), "rb") as f:
                data = f.read()
            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(data)
            with open(os.path.join(root, file), "wb") as f:
                f.write(encrypted_data)

def encrypt_file(filename, key):
    """
    Encrypts a single file
    """
    with open(filename, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(filename, "wb") as f:
        f.write(encrypted_data)

def decrypt_directory(path, key):
    """
    Recursively decrypts a directory and all its contents
    """
    for root, _, files in os.walk(path):
        for file in files:
            with open(os.path.join(root, file), "rb") as f:
                data = f.read()
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(data)
            with open(os.path.join(root, file), "wb") as f:
                f.write(decrypted_data)

def decrypt_file(filename, key):
    """
    Decrypts a single file
    """
    with open(filename, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)
    with open(filename, "wb") as f:
        f.write(decrypted_data)

# Generate a key
generate_key()

# Load the key
key = load_key()

# Encrypt a directory
path = "path/to/directory"
encrypt_directory(path, key)

# Decrypt a directory
path = "path/to/encrypted/directory"
decrypt_directory(path, key)

# Encrypt a file
filename = "path/to/file"
encrypt_file(filename, key)

# Decrypt a file
filename = "path/to/encrypted/file"
decrypt_file(filename, key)

# source: https://chat.openai.com/
