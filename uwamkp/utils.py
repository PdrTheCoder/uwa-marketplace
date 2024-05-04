"""
Here we can add some help function if you need.
"""
import hashlib
import random
import string


def get_salt_and_password(password: str, salt=None) -> tuple:
    """generate the pair of hashed password and salt using plain password"""
    letters = string.ascii_lowercase
    if not salt:
        salt = ''.join([random.choice(letters) for _ in range(8)])
    return (hashlib.md5((password + salt).encode('utf-8')).hexdigest(), salt)


def check_password(password, saved, salt):
    return hashlib.md5((password + salt).encode('utf-8')).hexdigest() == saved
