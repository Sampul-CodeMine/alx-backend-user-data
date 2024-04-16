#!/usr/bin/env python3
""" Module of Authenitcation """
from flask import request
from typing import List, TypeVar


class Auth:
    """This is a class that implements User's authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This is a public method to check if a path requires authentication.

        Args:
            path(str): The path to navigate to.
            excluded_paths(List[str]): a list of path to exclude from the
            search.

        Returns:
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        This is a public method to return authorization header for a request.

        Args:
            request(optional): default for the request is None

        Returns:
            None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This is a public method to return an instance of the current user.

        Args:
            request(optional): default for the request is None

        Returns:
            None
        """
        return None
