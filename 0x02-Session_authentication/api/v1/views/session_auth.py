#!/usr/bin/env python3
""" Module of SessionAuth views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login session"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400

    users = User.search({'email': email})
    if not users or len(users) == 0:
        return jsonify({ "error": "no user found for this email" }), 404

    user_ui = None
    for user in users:
        if user.is_valid_password(user.password):
            user_ui = user

    if user_ui is None:
        jsonify({ "error": "wrong password" }), 401
    else:
        from api.v1.app import auth
        key = auth.create_session(user_ui.id)
    user_ui.set_cookie(getenv('SESSION_NAME'), key)
    return user_ui.to_json()