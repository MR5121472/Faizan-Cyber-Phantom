from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def get_cipher(key):
    return Fernet(key)

def encrypt_data(cipher, data):
    return cipher.encrypt(data.encode())

def decrypt_data(cipher, encrypted_data):
    return cipher.decrypt(encrypted_data).decode()
