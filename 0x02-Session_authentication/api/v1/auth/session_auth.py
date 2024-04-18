#!/usr/bin/env python3
""" Module of Authenitcation using Session Authentication"""
from flask import request
from uuid import uuid4 as uid
from api.v1.auth.auth import Auth
from models.user import User


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
