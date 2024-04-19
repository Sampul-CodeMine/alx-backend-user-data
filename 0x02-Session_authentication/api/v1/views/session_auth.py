#!/usr/bin/env python3
"""This is a moduke to authenticate session views
"""
import os
from flask import abort, jsonify, request
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def user_login():
    """This is a function to log user in using the POST method in the route
    POST /api/v1/auth_session/login

    Returns:
        JSON repr of a User object
    """
    email = request.form.get('email')
    passwd = request.form.get('password')
    if email is None or len(email.strip()) == 0:
        return jsonify({'error': 'email missing'}), 400
    if passwd is None or len(passwd.strip()) == 0:
        return jsonify({'error': 'password missing'}), 400

    try:
        users_obj = User.search({'email': email})
        if not users_obj or users_obj == [] or len(users_obj) == 0:
            return jsonify({'error': 'no user found for this email'}), 404
        for user in users_obj:
            if user.is_valid_password(passwd):
                from api.v1.app import auth
                sess_id = auth.create_session(user.id)
                data = jsonify(user.to_json())
                data.set_cookie(os.environ.get('SESSION_NAME'), sess_id)
                return data
        return jsonify({'error': 'wrong password'}), 401
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def user_logout():
    """This is a function to delete a session id and log out the user
    using the DELETE method in the route POST /api/v1/auth_session/logout

    Returns:
        JSON repr of an empty dictionary
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
