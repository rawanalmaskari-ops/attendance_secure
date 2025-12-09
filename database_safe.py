import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

DB_FILE = "users_secure.json"

def load_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump({"users": []}, f)
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_user(username, password):
    # منع الرموز غير المسموح بها
    if not username.isalnum():
        return False

    db = load_db()
    # هاش كلمة المرور
    password_hash = generate_password_hash(password)

    db["users"].append({
        "username": username,
        "password_hash": password_hash
    })
    save_db(db)
    return True

def verify_user(username, password):
    db = load_db()
    for user in db["users"]:
        if user["username"] == username:
            return check_password_hash(user["password_hash"], password)
    return False
