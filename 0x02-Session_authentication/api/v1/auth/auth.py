#!/usr/bin/env python3
"""class authorization"""
from flask import request
from typing import TypeVar, List
from os import getenv


class Auth:
    """class auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        exclus = []
        path_ = None
        if excluded_paths:
            for s in excluded_paths:
                if s[-1] == '*':
                    s = s[:len(s) - 1]
                exclus.append(s)
        if path:
            path_ = path + '/' if path[-1] != '/' else path[:len(path) - 1]
        if path is None or \
            (path not in exclus and path_ not in exclus) or \
                excluded_paths is None or len(excluded_paths) == 0:
            return True
        return None

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return request.headers.get('Authorization') if request else None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None

    def session_cookie(self, request=None):
        """
        seesion cookie
        """
        if request is None:
            return None
        _my_session_id = getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)
