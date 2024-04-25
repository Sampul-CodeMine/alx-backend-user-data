#!/usr/bin/env python3
""" A Basic Flask Application Module """
from flask import (Flask, abort, jsonify, request, redirect)
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


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0")
