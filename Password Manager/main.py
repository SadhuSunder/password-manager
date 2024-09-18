import auth
import storage
import password_generator
import backup

def main():
    storage.create_table()
    if auth.user_authentication():
        while True:
            print("1. Save new password")
            print("2. Retrieve a password")
            print("3. Generate password")
            print("4. Backup passwords")
            choice = input("Choose an option: ")

            if choice == '1':
                account = input("Enter account name: ")
                password = input("Enter the password: ")
                storage.save_password(account, password)

            elif choice == '2':
                account = input("Enter account name: ")
                print(storage.retrieve_password(account))

            elif choice == '3':
                length = int(input("Enter password length: "))
                print(f"Generated Password: {password_generator.generate_password(length)}")

            elif choice == '4':
                backup.backup_passwords()

            else:
                print("Invalid choice.")

if __name__ == '__main__':
    main()
