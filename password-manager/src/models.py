from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PasswordEntry:
    service: str
    username: str
    password: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())