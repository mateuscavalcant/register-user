import re


def validateEmail(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True


def validatePassword(password):
    if len(password) < 8 or len(password) > 20:
        return False
    return True
