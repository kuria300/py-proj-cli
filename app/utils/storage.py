import json
from pathlib import Path
from app.models.user import User

DIR= Path('app/data')

user_path=DIR / 'database.json'


def load_users(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

            # return [User.from_dict(u) for u in data]
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_users(file_path, data):
    with open(file_path, 'w') as f:
        # [user.to_dict() for user in data]
        json.dump(data, f, indent=4)