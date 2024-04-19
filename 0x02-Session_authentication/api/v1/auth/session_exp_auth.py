#!/usr/bin/env python3
""" Module of Authenitcation using Session Authentication with expiry"""
import os
from flask import request
from datetime import datetime, timedelta
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """This is a class that implements the Session functionalities
    But implements from the Session Auth Class created earlier
    so as to allow or implement expiration for cookies."""

    def __init__(self) -> None:
        """This is the class constructor
        """
        super().__init__()
        try:
            duration = int(os.environ.get('SESSION_DURATION'))
        except Exception:
            duration = 0
        self.session_duration = duration

    def create_session(self, user_id: str = None) -> str:
        """This is a class method that creates a session for the current user.

        Args:
            user_id (str, optional): Defaults to None.

        Returns:
            str: the generated session id
        """
        sess_id = super().create_session(user_id)
        if sess_id is None or type(sess_id) is not str:
            return None
        self.user_id_by_session_id[sess_id] = {
            'user_id': user_id, 'created_at': datetime.now()
        }
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
        if session_id not in self.user_id_by_session_id:
            return None
        session_data = self.user_id_by_session_id[session_id]
        if 'created_at' not in session_data:
            return None
        if self.session_duration <= 0:
            return session_data['user_id']
        start_time = datetime.now()
        duration = timedelta(seconds=self.session_duration)
        expry_time = session_data['created_at'] + duration
        if expry_time < start_time:
            return None
        return session_data['user_id']
