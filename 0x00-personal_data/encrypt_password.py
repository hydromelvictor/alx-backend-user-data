#!/usr/bin/env python3
"""
logging learning
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashage"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
