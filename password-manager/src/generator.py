import secrets
import string


def generate_password(length: int = 16, use_digits: bool = True, use_symbols: bool = True) -> str:
    alphabet = string.ascii_letters
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    return "".join(secrets.choice(alphabet) for _ in range(length))

