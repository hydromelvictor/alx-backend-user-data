#!/usr/bin/env python3
"""
register_user(email: str, password: str) -> None
log_in_wrong_password(email: str, password: str) -> None
log_in(email: str, password: str) -> str
profile_unlogged() -> None
profile_logged(session_id: str) -> None
log_out(session_id: str) -> None
reset_password_token(email: str) -> str
update_password(email: str, reset_token: str, new_password: str) -> None
"""
import requests
from flask import url_for
import json


def register_user(email: str, password: str) -> None:
    """"""
    payload = {'email': email, 'password': password}
    response = {"email": f"{email}", "message": "user created"}
    req = requests.get(url_for('users'), params=payload)
    assert req.status_code == 200
    assert req.text == json.dumps(response)


def log_in_wrong_password(email: str, password: str) -> None:
    """"""
    payload = {'email': email, 'password': password}
    req = requests.get(url_for('login'), params=payload)
    assert req.status_code == 401


def log_in(email: str, password: str) -> str:
    """"""
    payload = {'email': email, 'password': password}
    response = {"email": f"{email}", "message": "logged in"}
    req = requests.get(url_for('login'), params=payload)
    assert req.status_code == 200
    assert req.text == json.dumps(response)
    return req.text


def profile_unlogged() -> None:
    """"""
    req = requests.get(url_for('profile'))
    assert req.status_code == 403


def profile_logged(session_id: str) -> None:
    """"""
    response = {"email": f"{user.email}"}
    req = requests.get(url_for('profile'))
    assert req.status_code == 200
    assert req.text == json.dumps(response)


def log_out(session_id: str) -> None:
    """"""
    payload = {'session_id': session_id}
    req = requests.get(url_for('logout'), params=payload)
    assert req.status_code == 200


def reset_password_token(email: str) -> str:
    """"""
    payload = {'email': email}
    response = {"email": f"{email}", "reset_token": f"{reset_token}"}
    req = requests.get(url_for('get_reset_password'), params=payload)
    assert req.status_code == 200
    assert req.text == json.dumps(response)
    return req.text


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """"""
    payload = {'email': email, 'reset_token': reset_token,
               'new_password': new_password}
    response = {"email": f"{email}", "message": "Password updated"}
    req = requests.get(url_for('reset_password'), params=payload)
    assert req.status_code == 200
    assert req.text == json.dumps(response)


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
