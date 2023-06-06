#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User

UserArgs = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
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
        """new user"""
        if email and hashed_password:
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
            return user

    def find_user_by(self, **kwargs) -> User:
        """
        keywordargument
        """
        if kwargs:
            if any(key not in UserArgs for key in kwargs):
                raise InvalidRequestError
            user = self._session.query(User).filter_by(**kwargs).first()
            if not user:
                raise NoResultFound
            return user
        else:
            raise InvalidRequestError

    def update_user(self, id: int, **kwargs) -> None:
        """update user"""
        for key in kwargs:
            if key not in UserArgs:
                raise ValueError
        try:
            user = self.find_user_by(**kwargs)
            for key, val in kwargs.items():
                setattr(user, key, val)
            return None
        except Exception:
            return None
