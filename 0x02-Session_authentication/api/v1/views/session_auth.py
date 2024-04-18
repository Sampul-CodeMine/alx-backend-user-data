#!/usr/bin/env python3
"""This is a moduke to authenticate session views
"""
import os
from flask import abort, jsonify, request
from models.user import User
from api.v1.views import app_views
from typing import Tuple


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def user_login() -> Tuple[str, int]:
    """This is a function to log user in using the POST method in the route
    POST /api/v1/auth_session/login
    
    Returns:
        JSON repr of a User object
    """
    email = request.form.get('email')
    passwd = request.form.get('password')
    if email is None or len(email) == 0:
        return jsonify({'error': 'email missing'}), 400
    if passwd is None or len(passwd) == 0:
        return jsonify({'error': 'password missing'}), 400
    
    try:
        users_obj = User.search({'email': email})
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404
    if not len(users_obj) > 0:
        return jsonify({'error': 'no user found for this email'}), 404
    if users_obj[0].is_valid_password(passwd):
        from api.v1.app import auth
        sess_id = auth.create_session(getattr(users_obj[0], 'id'))
        data = jsonify(users_obj[0].to_json())
        data.set_cookie(os.environ.get('SESSION_NAME', sess_id))
        return data
    return jsonify({'error': 'wrong password'})
