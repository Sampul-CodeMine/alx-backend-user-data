#!/usr/bin/env python3
""" Module of Authenitcation using Session Authentication stored in a DB"""
from flask import request
from datetime import datetime, timedelta
from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """This is a class that implements the Session functionalities
    But implements from the SessionExpAuth Class created earlier
    so as to allow or implement expiration for cookies or sessions stored
    in a Database."""

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
        sess_data = {
            'user_id': user_id,
            'session_id': sess_id
        }
        user_sess = UserSession(**sess_data)
        user_sess.save()
        return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """This is a method that gets a User ID from a session id

        Args:
            session_id (str, optional): Defaults to None.

        Returns:
            str: The user ID from a Session ID
        """
        if session_id is None:
            return None
        try:
            session_data = UserSession.search({'session_id': session_id})
            start_time = datetime.now()
            duration = timedelta(seconds=self.session_duration)
            expry_time = session_data[0]['created_at'] + duration
            if expry_time < start_time:
                return None
            return session_data[0]['user_id']
        except Exception:
            return None

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
        user_sess = UserSession.search({'session_id': sess_id})
        if len(user_sess) <= 0:
            return False
        user_sess[0].remove()
        return True
