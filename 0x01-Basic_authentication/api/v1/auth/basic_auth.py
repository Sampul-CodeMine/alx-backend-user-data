#!/usr/bin/env python3
""" Module of Authenitcation using Basic Access Authentication"""
from typing import TypeVar, Tuple
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """This is a class that implements the Basic Auth functionalities
    But implements from the simple Auth Class created earlier."""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        This is a public method that returns a base64 part of an
        Authorization header for a Basic Access Authentication

        Args:
            authorization_header(str): header of the authorization request

        Returns:
            None if authorization_header is None or not a string or doesnt
            start by Basic with a space at the end
            (str) - The string or value after the word Basic
        """
        if ((authorization_header is None) or
           (type(authorization_header) is not str) or
           (not authorization_header.startswith('Basic '))):
            return None
        return authorization_header.split(" ")[-1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """This is a public method that implements decoding a base64 encoded
        data into plain string

        Args:
            base64_authorization_header(str): encoded base64 string

        Returns:
            None if base64_authorization_header is None or not a string or
            is not a valid base64 string
            (str) - The decoded utf-8 string or value
        """
        if ((base64_authorization_header is None) or
           (type(base64_authorization_header) is not str)):
            return None
        try:
            token = base64.b64decode(base64_authorization_header,
                                     validate=True)
            return token.decode('utf-8')
        except (UnicodeDecodeError, Exception):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """
        This is a method that retrieves the email and password from a decoded
        base64 string and returns the extracted or retrieved email/password

        Args:
             decoded_base64_authorization_header(str): Decoded base64 string

        Returns:
            (str, str)(tuple): a tuple with the value of email and password
            If not found or decoded value not valid, then return a tuple of
            (None, None)
        """
        if ((decoded_base64_authorization_header is None) or
           (type(decoded_base64_authorization_header) is not str) or
           (':' not in decoded_base64_authorization_header)):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """
        This is a method that returns the instance of a User object based on
        the email and password retrieved.

        Args:
            user_email(str): email retrieved from decoded base64 header
            user_pwd(str): password retrieved from decoded based64 header

        Returns:
            User(Instance of the User object)
        """
        if ((user_email is None) or (not isinstance(user_email, str)) or
           (user_pwd is None) or (not isinstance(user_pwd, str))):
            return None
        try:
            users_obj = User.search({'email': user_email})
            if not users_obj or users_obj == []:
                return None
            for user in users_obj:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This is a method that returns the instance of a User object based on
        the request received.

        Args:
            request: Default is None

        Returns:
            User(Instance of the User object)
        """
        auth_header = self.authorization_header(request)
        b64_token = self.extract_base64_authorization_header(auth_header)
        token = self.decode_base64_authorization_header(b64_token)
        email, pwd = self.extract_user_credentials(token)
        return self.user_object_from_credentials(email, pwd)
