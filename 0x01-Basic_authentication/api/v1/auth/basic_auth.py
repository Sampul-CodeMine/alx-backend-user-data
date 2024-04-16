#!/usr/bin/env python3
""" Module of Authenitcation using Basic Access Authentication"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """This is a class that implements the Basic Auth functionalities
    But implements from the simple Auth Class created earlier."""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        This is a puvblic method that returns a base64 part of an
        Authorization header for a Basic Access Authentication

        Args:
            authorization_header(str): header of the authorization request

        Returns:
            None if authorization_header is None or not a string or doesnt start
            by Basic with a space at the end
            (str) - The string or value after the word Basic
        """
        if ((authorization_header is None) or
            (type(authorization_header) is not str) or
            (not authorization_header.startswith('Basic '))):
            return None
        return authorization_header.split(" ")[-1]
