#!/usr/bin/env python3
""" Module of Authenitcation using Basic Access Authentication"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64


class BaseAuth(Auth):
    """This is a class that implements the Basic Auth functionalities
    But implements from the simple Auth Class created earlier."""
    pass
