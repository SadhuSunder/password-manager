import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
import storage  # Your storage file with SQLite interaction
import encryption  # Your encryption file with password encryption/decryption logic
import password_generator  # Your password generation module

# Main window
class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Manager")
        self.root.geometry("400x400")

        # Entry for Account Name
        self.account_label = tk.Label(root, text="Account Name:")
        self.account_label.pack(pady=5)
        self.account_entry = tk.Entry(root, width=40)
        self.account_entry.pack(pady=5)

        # Entry for Password
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*", width=40)
        self.password_entry.pack(pady=5)

        # Button to Add Password
        self.add_button = tk.Button(root, text="Add Password", command=self.add_password)
        self.add_button.pack(pady=10)

        # Button to Generate Password
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Button to Retrieve Password
        self.retrieve_button = tk.Button(root, text="Retrieve Password", command=self.retrieve_password)
        self.retrieve_button.pack(pady=10)

        # Text box for showing passwords
        self.output_text = ScrolledText(root, width=40, height=10)
        self.output_text.pack(pady=10)

    def add_password(self):
        account = self.account_entry.get()
        password = self.password_entry.get()

        if account and password:
            # Encrypt the password
            encrypted_password = encryption.encrypt_password(password)

            # Save to the database
            storage.save_password(account, encrypted_password)
            messagebox.showinfo("Success", f"Password for {account} added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in both account and password.")

    def generate_password(self):
        # Generate a strong password using the password generator module
        generated_password = password_generator.generate_strong_password()
        self.password_entry.delete(0, tk.END)  # Clear the password field
        self.password_entry.insert(0, generated_password)  # Insert the generated password

    def retrieve_password(self):
        account = self.account_entry.get()

        if account:
            # Retrieve encrypted password from the database
            encrypted_password = storage.get_password(account)
            if encrypted_password:
                # Decrypt the password
                decrypted_password = encryption.decrypt_password(encrypted_password)
                self.output_text.insert(tk.END, f"Account: {account}\nPassword: {decrypted_password}\n\n")
            else:
                messagebox.showwarning("Not Found", "No password found for this account.")
        else:
            messagebox.showwarning("Input Error", "Please enter the account name.")

    def clear_entries(self):
        self.account_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
