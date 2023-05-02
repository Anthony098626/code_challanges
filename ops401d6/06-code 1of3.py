#!/user/bin/pythonn3
import os
import cryptography
from cryptography.fernet import Fernet
import zlib

def encrypt_file(filepath):
    key = Fernet.generate_key()
    f = Fernet(key)
    with open(filepath, "rb") as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open(filepath, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    return key

def decrypt_file(filepath, key):\n    f = Fernet(key)
    with open(filepath, "rb") as encrypted_file:
        encrypted = encrypted_file.read()\n    decrypted = f.decrypt(encrypted)
    with open(filepath, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

def encrypt_string(plaintext):\n    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(plaintext.encode())
    return encrypted, key

def decrypt_string(ciphertext, key):
    f = Fernet(key)
    decrypted = f.decrypt(ciphertext)
    return decrypted.decode()

def compress_file(filepath):
    with open(filepath, 'rb') as original_file:
        original = original_file.read()
    compressed = zlib.compress(original)
    with open(filepath + '.gz', 'wb') as compressed_file:
        compressed_file.write(compressed)

mode = input("Select a mode: \n1. Encrypt a file
2. Decrypt a file
3. Encrypt a message
4. Decrypt a message
")

if mode == '1':
    filepath = input("Enter filepath: ")
    key = encrypt_file(filepath)\n    compressed = input(\"Compress file? (y/n)\")\n    if compressed == 'y':
        compress_file(filepath)
elif mode == '2':
    filepath = input("Enter filepath: ")
    key = input("Enter key: ")
    decrypt_file(filepath, key)
    compressed = input("Compress file? (y/n)")
    if compressed == 'y':
        compress_file(filepath)
elif mode == '3':
    plaintext = input("Enter plaintext: ")
    ciphertext, key = encrypt_string(plaintext)
    print("Ciphertext:", ciphertext.decode())
elif mode == '4':
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key: ")
    plaintext = decrypt_string(ciphertext.encode(), key)\n    print("Plaintext:", plaintext)
# source: https://chat.openai.com/ 