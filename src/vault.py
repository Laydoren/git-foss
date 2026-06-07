from src.models import PasswordEntry
from src.storage import load_entries, save_entries
from src.generator import generate_password


class EntryNotFoundError(Exception):
    pass


def add_entry(service: str, username: str, password: str) -> None:
    entries = load_entries()
    entries.append(PasswordEntry(service=service, username=username, password=password))
    save_entries(entries)


def list_entries() -> list[PasswordEntry]:
    entries = load_entries()
    if not entries:
        raise EntryNotFoundError("No passwords saved yet.")
    return entries


def get_entry(service: str) -> PasswordEntry:
    entries = load_entries()
    for entry in entries:
        if entry.service.lower() == service.lower():
            return entry
    raise EntryNotFoundError(f"No entry found for service: {service}")


def delete_entry(service: str) -> None:
    entries = load_entries()
    new_entries = [e for e in entries if e.service.lower() != service.lower()]
    if len(new_entries) == len(entries):
        raise EntryNotFoundError(f"No entry found for service: {service}")
    save_entries(new_entries)


def generate_and_add(service: str, username: str, length: int = 16) -> str:
    password = generate_password(length=length)
    add_entry(service, username, password)
    return password