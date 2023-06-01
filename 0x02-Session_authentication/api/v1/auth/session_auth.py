#!/usr/bin/env python3
"""session authentication"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """inheritance by auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        description
        ==============

        parameters
        ===========
        user_id : str

        __return__  : str
        ===========
        """
        if user_id is None and type(user_id) is not str:
            return None
        key = str(uuid4())
        self.user_id_by_session_id[key] = user_id
        return key

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        description
        ==============

        parameters
        ===========
        session_id : str

        __return__  : str
        ===========
        """
        if session_id is None and type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """current user"""
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)
