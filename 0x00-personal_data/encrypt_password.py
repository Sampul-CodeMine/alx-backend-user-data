#!/usr/bin/env python3
"""This is a module for Data Encryption using the BCRYPT library
This is to help with hashing or encrypting PII and PD
"""
import bcrypt as bc


def hash_password(password: str) -> bytes:
    """This is a function that hashes plain-text passwords
    into salted hashed strings of characters using bcrypt library.

    Args:
        password (str): the plaintext string passed or entered by users

    Returns:
        (bytes) - The hashed or encrypted password
    """
    if password:
        return bc.hashpw(password.encode(), bc.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This is a function that verifies a plaintext password against a hashed
    password:
    The function cross-checkes if the plaintext passed by the user as a
    password exactly matches the hashed password saved in a database

    Args:
        hashed_password (bytes): the password stored in the DB
        password (str): the string or plaintext password provided on login

    Returns:
        (bool): True if it matches else False
    """
    if password and hashed_password:
        return True if bc.checkpw(password.encode(),
                                  hashed_password) else False
