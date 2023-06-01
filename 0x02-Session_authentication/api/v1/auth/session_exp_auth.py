#!/usr/bin/env python3
"""session authentication"""

from api.v1.auth.session_auth import SessionAuth
from uuid import uuid4
from models.user import User
from os import getenv
from datetime import datetime


class SessionExpAuth(SessionAuth):
    """expirate date to session"""

    def __init__(self):
        """initialisation session"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0
    
    def create_session(self, user_id=None):
        """create session"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id['created_at'] = datetime.now()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user id for session id"""
        if not session_id or not self.user_id_by_session_id.get(session_id):
            return None
        
