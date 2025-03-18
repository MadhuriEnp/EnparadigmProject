import random
import string

def generate_random_string(length=10):
    """Generate a random string of specified length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_string_with_prefix(length=10, prefix="test"):
    """Generate a random string of specified length starting with a given prefix."""
    if length <= len(prefix):
        raise ValueError("Length must be greater than the length of the prefix")
    remaining_length = length - len(prefix)
    letters = string.ascii_letters + string.digits
    random_part = ''.join(random.choice(letters) for _ in range(remaining_length))
    return prefix + random_part


def generate_random_name_with_prefix(prefix, name_length=6):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    random_name = ''.join(random.choice(characters) for _ in range(name_length))
    return prefix + random_name.capitalize()
    random_name = generate_random_name_with_prefix(prefix="Krishna", name_length=5)
    print(random_name)

def generate_random_email(length=10, domain="example.com"):
    """Generate a random email address with a specified length and domain."""
    letters = string.ascii_letters + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    return f"{username}@{domain}"
