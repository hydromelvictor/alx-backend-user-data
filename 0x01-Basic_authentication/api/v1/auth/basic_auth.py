#!/usr/bin/env python3
"""Create a class BasicAuth that inherits from Auth.
For the moment this class will be empty.
"""
from auth.auth import Auth
from flask import request
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """basic authorization"""
    
    def extract_base64_authorization_header(self, \
        authorization_header: str) -> str:
        """
        description
        ============

        parameters
        ============
        authorization_header: str

        __return__ : str
        """
        if authorization_header and type(authorization_header) == str:
            if authorization_header.split(' ')[0] == 'Basic':
                return authorization_header.split(' ')[1]
        return None

    def decode_base64_authorization_header(self, \
        base64_authorization_header: str) -> str:
        """
        description
        ============

        parameters
        ============
        base64_authorization_header: str

        __return__ : str
        """
        if base64_authorization_header and \
            type(base64_authorization_header) == str:
            try:
                return base64.b64decode(base64_authorization_header)\
                    .decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(self, \
        decoded_base64_authorization_header: str) -> (str, str):
        """
        description
        ============

        parameters
        ============
        decoded_base64_authorization_header: str

        __return__ : tuple
        """
        if decoded_base64_authorization_header and \
            type(decoded_base64_authorization_header) == str:
            if len(decoded_base64_authorization_header) != 0:
                tab = tuple(decoded_base64_authorization_header.split(':'))
                return tab[0], ':'.join(tab[1:])
        return None
        
    def user_object_from_credentials(self, user_email: str, \
        user_pwd: str) -> TypeVar('User'):
        """
        description
        ============

        parameters
        ============
        user_email: str
        user_pwd: str

        __return__ : tuple
        """
        if (user_email and type(user_email) == str) or \
            (user_pwd and type(user_pwd)):
            user = {'email': user_email, '_password': user_pwd}
            if User.count() == 0:
                return User(user)
            truely = User.search({'email': user_email})
            if truely:
                for elt in truely[User.__name__].values():
                    if elt.is_valid_password(user_pwd):
                        return User(user)
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        description
        ============

        parameters
        ============
        request=None

        __return__: TypeVar('User')
        """
        authorization_header = self.authorization_header(request)
        base64_authorization_header = \
            self.extract_base64_authorization_header(authorization_header)
        decoded_base64_authorization_header = \
            self.decode_base64_authorization_header(base64_authorization_header)
        user = self.user_object_from_credentials(self.extract_user_credentials \
            (decoded_base64_authorization_header))
        return user
