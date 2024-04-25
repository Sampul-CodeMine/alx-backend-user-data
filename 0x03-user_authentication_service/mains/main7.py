#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email1 = 'bob@bob.com'
password1 = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email1, password1)

print(auth.create_session(email1))
print(auth.create_session("unknown@email.com"))


email2 = 'tega@em.com'
password2 = 'myPassword'

auth.register_user(email2, password2)

print(auth.create_session(email2))
