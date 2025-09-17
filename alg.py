import curses.ascii


def outer(name):
    def inner():
        print( f"Hello, {name}!")
    return inner

def create(s):
    return lambda x: x == s


def create_account(user_name, password, secret_words):
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long")

    has_up = any(char.isupper() for char in password)
    has_low = any(char.islower() for char in password)
    has_dig = any(char.isdigit() for char in password)
    has_sp = any(char in "!:;.,&?/|\\][{}-@#$%^&*()_+" for char in password)

    if not (has_up and has_low and has_dig and has_sp):
        raise ValueError(
            "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character")

    from collections import Counter

    def check(input_password, input_secret_words):
        if input_password != password:
            return False

        if len(input_secret_words) != len(secret_words):
            return False

        c_orig = Counter(secret_words)
        c_inp = Counter(input_secret_words)
        matches = sum(min(c_orig[k], c_inp[k]) for k in set(c_orig) | set(c_inp))
        mismatches = len(secret_words) - matches
        return mismatches <= 1

    return check

def divisor(num):
    for d in range(1, num + 1):
        if num % d == 0:
            yield d
    while True:
        yield None


