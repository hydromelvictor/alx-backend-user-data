#!/usr/bin/env python3
"""
Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload
of the form
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """
    salutation
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users/<email>/<password>', methods=['POST'], strict_slashes=False)
def users(email, password) -> str:
    """all users"""
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login authentication"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        resp = jsonify({"email": f"{email}", "message": "logged in"})
        resp.set_cookie("session_id", session_id)
        return resp
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ logout authentication """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ user profile """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": f"{user.email}"}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ reset password """
    email = request.form.get('email')
    if email:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": f"{email}", "reset_token": f"{reset_token}"})
    abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ update password """
    email = request.form.get("email")
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    if reset_token:
        return jsonify({"email": f"{email}",
                        "message": "Password updated"}), 200
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
