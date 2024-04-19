#!/usr/bin/env python3
"""This is a module for User Session Model to a DB"""
from models.base import Base


class UserSession(Base):
    """Class to model a User Session DB table

    Args:
        Base (ParentClass): This is the parent class from which
        UserSession class inherits
    """
    def __init__(self, *args: list, **kwargs: dict):
        """This is a constructor to initialize UserSession instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
