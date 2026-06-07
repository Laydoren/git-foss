import pytest

from src.generator import check_strength, generate_password
from src.vault import (
    EntryNotFoundError,
    add_entry,
    delete_entry,
    generate_and_add,
    get_entry,
    list_entries,
)


def test_generate_password_default_length() -> None:
    pwd = generate_password()
    assert len(pwd) == 16


def test_generate_password_custom_length() -> None:
    pwd = generate_password(length=24)
    assert len(pwd) == 24


def test_generate_password_no_symbols() -> None:
    import string

    pwd = generate_password(use_symbols=False)
    assert not any(c in string.punctuation for c in pwd)


def test_generate_password_no_digits() -> None:
    pwd = generate_password(use_digits=False)
    assert not any(c.isdigit() for c in pwd)


def test_check_strength_weak() -> None:
    assert check_strength("abc") == "weak"


def test_check_strength_strong() -> None:
    assert check_strength("Abcdef1!Abcdef1!") == "strong"


def test_add_and_get_entry(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("src.storage.DATA_FILE", tmp_path / "vault.json")
    add_entry("github", "user", "secret123")
    entry = get_entry("github")
    assert entry.service == "github"
    assert entry.username == "user"
    assert entry.password == "secret123"


def test_get_entry_case_insensitive(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("src.storage.DATA_FILE", tmp_path / "vault.json")
    add_entry("GitHub", "user", "secret123")
    entry = get_entry("github")
    assert entry.service == "GitHub"


def test_get_entry_not_found(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("src.storage.DATA_FILE", tmp_path / "vault.json")
    with pytest.raises(EntryNotFoundError):
        get_entry("nonexistent")


def test_delete_entry(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("src.storage.DATA_FILE", tmp_path / "vault.json")
    add_entry("github", "user", "secret123")
    delete_entry("github")
    with pytest.raises(EntryNotFoundError):
        get_entry("github")


def test_delete_entry_not_found(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("src.storage.DATA_FILE", tmp_path / "vault.json")
    with pytest.raises(EntryNotFoundError):
        delete_entry("nonexistent")


def test_list_entries(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("src.storage.DATA_FILE", tmp_path / "vault.json")
    add_entry("github", "user1", "pass1")
    add_entry("gitlab", "user2", "pass2")
    entries = list_entries()
    assert len(entries) == 2
    assert entries[0].service == "github"
    assert entries[1].service == "gitlab"


def test_list_entries_empty(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("src.storage.DATA_FILE", tmp_path / "vault.json")
    with pytest.raises(EntryNotFoundError):
        list_entries()


def test_generate_and_add(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("src.storage.DATA_FILE", tmp_path / "vault.json")
    password = generate_and_add("github", "user", length=20)
    assert len(password) == 20
    entry = get_entry("github")
    assert entry.password == password
