#!/usr/bin/env python3
"""This is a module to authenticate users"""
import bcrypt
from db import DB
from uuid import uuid4 as uid
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


def _generate_uuid() -> str:
    """This is a function to generate UUID 4 strings

    Returns:
        generated uuid string token
    """
    return str(uid())


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

    def valid_login(self, email: str, password: str) -> bool:
        """This is a method to validate user Login

        Args:
            email(str, required): This is the email of the user to login
            password(str, required): The plaintext password of user to login

        Returns:
            (bool): True if login validated else False
        """
        try:
            user = self._db.find_user_by(email=email)
            pwd = password.encode('utf-8')
            return bcrypt.checkpw(pwd, user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """This is a method to create a session for a validated user

        Args:
            email(str, required): The email of the user to create session for

        Returns:
            (str): The session_id created for the user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                sess_id = _generate_uuid()
                user.session_id = sess_id
                return sess_id
            return None
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """This is a method to get a User details from the seesion ID of the
        currently logged in or validated user.

        Args:
            session_id(str, required): The session_id of the currently logged
            in user

        Returns:
            If found return User(obj) else return None
        """
        if session_id is not None:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user if user is not None else None
            except (NoResultFound, Exception):
                return None
        return None

    def destroy_session(self, user_id: int) -> None:
        """This is a method to destroy the session of the currently validated
        or logged in user and update their session_id attribute

        Args:
            user_id(int, required): The user_id of the currently logged
            in user

        Returns:
            None
        """
        if user_id is not None:
            try:
                self._db.update_user(user_id, session_id=None)
            except NoResultFound:
                return None
        return None
