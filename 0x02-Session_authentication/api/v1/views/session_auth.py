#!/usr/bin/env python3
"""
Create a new Flask view that handles all routes for the
Session authentication
"""
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login user me"""

    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            me = user
            from api.v1.app import auth
            key = auth.create_session(me.id)
            json_me = jsonify(me.to_json())
            json_me.set_cookie(getenv('SESSION_NAME'), key)
            return json_me
        else:
            return jsonify({"error": "wrong password"}), 401
    return jsonify({"error": "no user found for this email"}), 404


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """logout"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
