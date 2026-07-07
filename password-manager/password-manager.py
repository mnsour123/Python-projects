import os
import base64
from getpass import getpass

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken

DATA_FILE = "passwords.txt"
SALT_FILE = "salt.bin"


def get_salt():
    """Load the existing salt or create a new one on first run."""
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)
    return salt


def derive_key(master_password, salt):
    """Turn the master password into a Fernet-compatible encryption key."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480_000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))


def view(fernet):
    if not os.path.exists(DATA_FILE):
        print("No passwords saved yet.")
        return

    with open(DATA_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                decrypted = fernet.decrypt(line.encode()).decode()
                user, passw = decrypted.split("|", 1)
                print(f"user: {user}, password: {passw}")
            except InvalidToken:
                print("Could not decrypt an entry — wrong master password?")


def add(fernet):
    name = input("account name: ")
    password = getpass("password: ")  # hides input as it's typed
    data = f"{name}|{password}"
    encrypted = fernet.encrypt(data.encode())

    with open(DATA_FILE, "a") as f:
        f.write(encrypted.decode() + "\n")
    print("Saved.")


def main():
    master_pwd = getpass("What is your master password? ")
    salt = get_salt()
    key = derive_key(master_pwd, salt)
    fernet = Fernet(key)

    while True:
        mode = input(
            "Would you like to add a password or see the existing ones? "
            "(view, add), press q to quit: "
        ).lower()

        if mode == "q":
            break
        elif mode == "view":
            view(fernet)
        elif mode == "add":
            add(fernet)
        else:
            print("Invalid answer")


if __name__ == "__main__":
    main()
