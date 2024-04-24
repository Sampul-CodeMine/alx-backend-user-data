#!/usr/bin/env python3
"""This is a module to Represent a DB"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """This is a method to add a user to the database

        Args:
            email(str): the email address of the user
            hashed_password(str): the hashed password for the user

        Returns:
            User(obj): The instance of the user added.
        """
        try:
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            user = None
        finally:
            return user

    def find_user_by(self, **kwargs: dict) -> User:
        """This is a method to find a user from the database

        Args:
            kwargs(dict): keyworded argument with which to search for user

        Returns:
            User(obj): The instance of the user found.
        """
        users = self._session.query(User)
        for field, value in kwargs.items():
            if field not in User.__dict__:
                raise InvalidRequestError
            for user in users:
                if getattr(user, field) == value:
                    return user
        raise NoResultFound
