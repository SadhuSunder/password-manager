import storage

def backup_passwords(filename="backup.txt"):
    with open(filename, "w") as file:
        storage.cursor.execute("SELECT * FROM passwords")
        for row in storage.cursor.fetchall():
            file.write(f"{row[1]},{row[2]}\n")
    print(f"Backup saved to {filename}.")
