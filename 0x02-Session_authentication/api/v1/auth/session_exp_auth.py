#!/usr/bin/env python3
"""session authentication"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


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
        self.user_id_by_session_id[session_id]['user_id'] = user_id
        self.user_id_by_session_id[session_id]['created_at'] = datetime.now()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user id for session id"""
        if not session_id or not self.user_id_by_session_id.get(session_id):
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id].get('user_id')
        if not self.user_id_by_session_id[session_id].get('created_at'):
            return None
        created_at = self.user_id_by_session_id[session_id].get('created_at')
        process = self.session_duration + timedelta(0, created_at)
        if datetime.now() - timedelta(self.session_duration.day,
                                      self.session_duration.second) > 0:
            None
        return self.user_id_by_session_id[session_id].get('user_id')
