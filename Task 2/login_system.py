import os
import hashlib
import re
import time
import json
import random
import string

from getpass import getpass  # Secure password input

os.environ['ADMIN_PASS'] = 'Pa$$w0rd123'

# Password salting function
def salt_and_hash(password, salt):
    salted = password + salt
    return hashlib.sha256(salted.encode()).hexdigest()

# User data simulate karo file-based "database"
db_file = "users_db.json"

# Agar file nahi hai to ek default user bana do
if not os.path.exists(db_file):
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    hashed_pass = salt_and_hash(os.environ['ADMIN_PASS'], salt)
    with open(db_file, "w") as f:
        json.dump({
            "admin": {
                "salt": salt,
                "password": hashed_pass,
                "attempts": 0
            }
        }, f)

# Validation Function
def validate_input(username, password):
    if not username or not password:
        print("Bhai input khali nahi chalay ga.")
        return False

    if len(password) < 8:
        print("Kamzor password! 8 characters chahiye.")
        return False

    if not re.search(r"[A-Z]", password):
        print("Password mein ek capital letter bhi hona chahiye.")
        return False

    if not re.search(r"[0-9]", password):
        print("Bhai ek number bhi hona chahiye password mein.")
        return False

    return True

# Login Function
def login_karo(username, password):
    with open(db_file, "r") as f:
        users = json.load(f)

    if username not in users:
        print("User exist nahi karta.")
        return

    user_data = users[username]

    # Brute-force limit
    if user_data["attempts"] >= 3:
        print("Zyada attempts ho gaye! Thori dair baad try karo.")
        return

    salt = user_data["salt"]
    hashed = salt_and_hash(password, salt)

    if hashed == user_data["password"]:
        print(f"Welcome {username}, tum login ho gaye!")
        users[username]["attempts"] = 0  # Reset attempts
    else:
        users[username]["attempts"] += 1
        print("Password galat hai. Attempts:", users[username]["attempts"])

    with open(db_file, "w") as f:
        json.dump(users, f)

# Entry Point
if __name__ == "__main__":
    print("🔐 Secure Login System")

    user = input("👤 Username daalo: ")
    pwd = getpass("🔑 Password chupke se daalo: ")

    if validate_input(user, pwd):
        login_karo(user, pwd)
