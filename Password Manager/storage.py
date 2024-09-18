import sqlite3
from encryption import encrypt_password, decrypt_password

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                      (id INTEGER PRIMARY KEY, account TEXT, password TEXT)''')
    conn.commit()

def save_password(account, password):
    encrypted_password = encrypt_password(password)
    cursor.execute("INSERT INTO passwords (account, password) VALUES (?, ?)", (account, encrypted_password))
    conn.commit()

def retrieve_password(account):
    cursor.execute("SELECT password FROM passwords WHERE account=?", (account,))
    result = cursor.fetchone()
    if result:
        return decrypt_password(result[0])
    return "Account not found."
