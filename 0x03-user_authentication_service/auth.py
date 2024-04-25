#!/usr/bin/env python3
"""This is a module to authenticate users"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """This is a function that hashes password entered by a user

    Args:
        password(str): plaintext password to be hashed

    Returns:
        (bytes) representation of the the hashed and salted password
    """
    return bcrypt.hashpw(password.encode("utf-8"),
                         bcrypt.gensalt())
