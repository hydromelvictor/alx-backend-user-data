#!/usr/bin/env python3
"""Create a folder api/v1/auth
Create an empty file api/v1/auth/__init__.py
Create the class Auth:
in the file api/v1/auth/auth.py
"""
from flask import request


class Auth:
    """Authorization class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        description
        ===========

        parameters
        ===========
        path: str
        excluded_paths: List[str]

        __return__: boolean
        """
        excluded_all = None
        if excluded_paths:
            excluded_all = [i[:len(i) - 1] for i in excluded_paths if i[-1] == '*']
        path0 = path + '/' if path[-1] != '/' else path[:len(path) - 1]
        if path is None or (path not in excluded_all and 
                            path0 not in excluded_all) \
                                or excluded_paths is None or \
                                    len(excluded_paths) == 0:
            return True
        return False
    
    def authorization_header(self, request=None) -> str:
        """
        description
        ============

        parameters
        ============
        request=None

        __return__: None
        """
        return request.headers.get('Authorization', None)
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        description
        ============

        parameters
        ============
        request=None

        __return__: TypeVar('User')
        """
        return None
