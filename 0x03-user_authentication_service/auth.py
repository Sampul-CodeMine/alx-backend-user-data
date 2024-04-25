#!/usr/bin/env python3
"""This is a module to authenticate users"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """This is a function that hashes password entered by a user

    Args:
        password(str): plaintext password to be hashed

    Returns:
        (bytes) representation of the the hashed and salted password
    """
    return bcrypt.hashpw(password.encode("utf-8"),
                         bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """This is a method to register a new user

        Args:
            email(str, required): This is the email of the user to register
            password(str, required): The password of the user to register

        Returns:
            User(obj): User object just registered.
        """
        try:
            self._db.find_user_by(email=email)  # try if user already exists
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))  # add user
        else:
            raise ValueError(f'User {email} already exists')  # raise an error
