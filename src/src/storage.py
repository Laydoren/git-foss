import json
from pathlib import Path
from src.models import PasswordEntry

DATA_FILE = Path("data/vault.json")


def load_entries() -> list[PasswordEntry]:
    if not DATA_FILE.exists():
        return []
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return [PasswordEntry(**item) for item in data]


def save_entries(entries: list[PasswordEntry]) -> None:
    DATA_FILE.parent.mkdir(exist_ok=True)
    data = [
        {
            "service": e.service,
            "username": e.username,
            "password": e.password,
            "created_at": e.created_at,
        }
        for e in entries
    ]
    DATA_FILE.write_text(json.dumps(data, indent=4), encoding="utf-8")