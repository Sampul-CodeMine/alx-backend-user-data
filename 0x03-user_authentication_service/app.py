#!/usr/bin/env python3
""" A Basic Flask Application Module """
from flask import (Flask, abort, jsonify, request, redirect, url_for)
from auth import Auth


app = Flask(__name__)
app.debug = False
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """This is the home route for the Basic Flask Application"""
    msg = {'message': 'Bienvenue'}
    return jsonify(msg)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """This is a route to register users"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            AUTH.register_user(email, password)
            msg = {'email': f"{email}", 'message': 'user created'}
            return jsonify(msg), 200
        except Exception:
            return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """This is a route to log users into the system"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if AUTH.valid_login(email, password):
            sess_id = AUTH.create_session(email)
            resp = jsonify({'email': email, 'message': 'logged in'})
            resp.set_cookie('session_id', sess_id)
            return resp
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """This is a route to log users out"""
    if request.method == 'DELETE':
        sess_id = request.cookies.get('session_id')
        user = AUTH.get_user_from_session_id(sess_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect(url_for('home'))
    abort(403)


# @app.route('/profile', methods=['GET'], strict_slashes=False)
# def user_profile() -> str:
#     """This is a route to display the users's profile"""
#     if request.method == 'GET':
#         sess_id = request.cookies.get('session_id')
#         user = AUTH.get_user_from_session_id(sess_id)
#         if user:
#             return jsonify({'email': f'{user.email}'}), 200
#     abort(403)


# @app.route('/reset_password', methods=['POST'], strict_slashes=False)
# def get_password_reset_token() -> str:
#     """This is a route to get a reset password token when a user request
#     for password change"""
#     if request.method == 'POST':
#         user_email = request.form.get('email')
#         try:
#             reset_token = AUTH.get_reset_password_token(user_email)
#             msg = {"email": f"{email}", "reset_token": f"{reset_token}"}
#         return jsonify(msg), 200
#         except ValueError:
#             abort(403)
#     abort(403)


# @app.route('/reset_password', methods=['PUT'], strict_slashes=False)
# def update_password() -> str:
#     """This is a route to reset the password"""
#     if request.method == 'PUT':
#         email = request.form.get('email')
#         reset_token = request.form.get('reset_token')
#         new_password = request.form.get('new_password')
#         try:
#             AUTH.update_password(reset_token, new_password)
#             msg = {"email": email, "message": "Password updated"}
#             return jsonify(msg), 200
#         except Exception:
#             abort(403)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0")
