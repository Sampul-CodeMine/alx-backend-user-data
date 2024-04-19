#!/usr/bin/env python3
""" Module of Authenitcation using Session Authentication"""
from flask import request
from uuid import uuid4 as uid
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class SessionAuth(Auth):
    """This is a class that implements the Session functionalities
    But implements from the simple Auth Class created earlier."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """This is a class method that creates a session for the current user.

        Args:
            user_id (str, optional): Defaults to None.

        Returns:
            str: the generated session id
        """
        if not type(user_id) == str or user_id is None:
            return None
        sess_id = str(uid())
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """This is a method that gets a User ID from a session id

        Args:
            session_id (str, optional): Defaults to None.

        Returns:
            str: The user ID from a Session ID
        """
        if not type(session_id) == str or session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None) -> TypeVar('User'):
        """This is a method that gets a User's object from a request

        Args:
            request (optional): Defaults to None.

        Returns:
            TypeVar('User): The User object from a request
        """
        print(self.user_id_for_session_id(self.session_cookie(request)))
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        print(user_id, User.get(user_id))
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """This is a method that deletes the current user's session and logout

        Args:
            request (optional): Defaults to None.

        Returns:
            True if session id was gotten from the request and session id is
            attached to a user ID else False
        """
        if request is None:
            return False
        sess_id = self.session_cookie(request)
        if sess_id is None:
            return False
        if self.user_id_for_session_id(sess_id) is None:
            return False
        del self.user_id_by_session_id[sess_id]
        return True
