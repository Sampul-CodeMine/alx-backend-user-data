#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# variable auth
auth = None

AUTH_TYPE = os.environ.get('AUTH_TYPE')

# check AUTH_TYPE
if AUTH_TYPE == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.before_request
def auth_before_request():
    """This method is run before the execution of any request to authenicate
    To authenticate request

    If auth is None - Does Nothing
    If request path is not in forbidden or unauthorized then do nothing
    """
    if auth is not None:
        excluded_paths = [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/',
            '/api/v1/auth_session/login/',
        ]
        if auth.require_auth(request.path, excluded_paths):
            auth_header = auth.authorization_header(request)
            sess_header = auth.session_cookie(request)
            user = auth.current_user(request)

            if auth_header is None and sess_header is None:
                abort(401)
            if user is None:
                abort(403)
            request.current_user = user
    else:
        pass


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
