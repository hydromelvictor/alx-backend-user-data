#!/usr/bin/env python3
"""class basicauth"""
from api.v1.auth.auth import Auth
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
