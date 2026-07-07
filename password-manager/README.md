# Simple Password Manager

A command-line password manager that encrypts saved credentials using a key
derived from your master password (PBKDF2-HMAC-SHA256 + Fernet/AES).

## Setup

```bash
pip install cryptography
python password_manager.py
```

## Usage

Enter your master password, then choose:

- `add` — save a new account name + password
- `view` — decrypt and list saved entries
- `q` — quit

## Files

- `salt.bin` — required for decryption; don't delete or lose it.
- `passwords.txt` — your encrypted entries.

## Note

For personal/educational use only — not audited for production use.
