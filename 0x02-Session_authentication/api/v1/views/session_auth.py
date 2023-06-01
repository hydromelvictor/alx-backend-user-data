#!/usr/bin/env python3
""" Module of SessionAuth views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login session"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    try :
        users = User.search({'email': email})
    except Exception:
        return jsonify({ "error": "no user found for this email" }), 404

    user_ui = None
    for user in users:
        if user.is_valid_password(password):
            user_ui = user
            from api.v1.app import auth
            key = auth.create_session(user_ui.id)
            user_json = jsonify(user_ui.to_json())
            user_json.set_cookie(getenv('SESSION_NAME'), key)
            return user_json
        else:
            return jsonify({ "error": "wrong password" }), 401
    return jsonify({ "error": "no user found for this email" }), 404
