#!/usr/bin/env python3
"""class basicauth"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """basic auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base64 authorization header"""
        if authorization_header and type(authorization_header) is str:
            if authorization_header.split(' ')[0] == 'Basic':
                return authorization_header.split(' ')[1]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode base64 authorization header"""
        if base64_authorization_header and \
                type(base64_authorization_header) is str:
            try:
                return base64.b64decode(
                    base64_authorization_header).decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """extract user credentials"""
        if decoded_base64_authorization_header and \
                type(decoded_base64_authorization_header) is str:
            if ':' in decoded_base64_authorization_header:
                tab = tuple(decoded_base64_authorization_header.split(':'))
                return tab[0], ':'.join(tab[1:])
        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user object from credentials"""
        user = {'email': user_email, '_password': user_pwd}
        if (user_email and type(user_email) is str) or \
                (user_pwd and type(user_pwd) is str):
            if User.count() == 0:
                User(user).save()
            truely = User.search({'email': user_email})
            if truely:
                for elt in truely[User.__name__].values():
                    if elt.is_valid_password(user_pwd):
                        return elt
        return None
