from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password).decode()
