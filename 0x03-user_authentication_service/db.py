#!/usr/bin/env python3
"""This is a module to Represent a DB"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

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
        if kwargs is None or not kwargs:
            raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()

        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """This is a method to update a user data in the  database

        Args:
            user_id(int): the user with id for which to update data
            kwargs(dict): keyworded argument with which to update user record

        Returns:
            Nothing
        """
        user = self.find_user_by(id=user_id)
        for field, value in kwargs.items():
            if hasattr(user, field):
                setattr(user, field, value)
            else:
                raise ValueError
        self._session.commit()
        return None
