import secrets
import string


def generate_password(length: int = 16, use_digits: bool = True, use_symbols: bool = True) -> str:
    alphabet = string.ascii_letters
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    return "".join(secrets.choice(alphabet) for _ in range(length))


def check_strength(password: str) -> str:
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "weak"
    if score <= 3:
        return "medium"
    return "strong"