#!/usr/bin/env python3
""" Module of Authenitcation using Session Authentication"""
from flask import request
from uuid import uuid4 as uid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """This is a class that implements the Session functionalities
    But implements from the simple Auth Class created earlier."""
    pass
