import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(stored_hash, entered_password):
    return stored_hash == hash_password(entered_password)

def user_authentication():
    username = input("Enter your username: ")
    stored_password_hash = hash_password("Sadhu123")
    entered_password = getpass.getpass("Enter your password: ")
    if check_password(stored_password_hash, entered_password):
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed!")
        return False
