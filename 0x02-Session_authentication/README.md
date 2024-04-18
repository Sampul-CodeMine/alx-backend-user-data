# 0x02. Session authentication - (Back-end | Authentification)

<p style="width: 350px; height: auto; margin: 5px auto;" align="center">
<img src="https://github.com/Sampul-CodeMine/alx-backend-user-data/blob/main/0x01-Basic_authentication/misc/failed_pass.png" alt="You Shall Not Pass" style="width: 300px;" align="center"></p>

## Background Context

In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://flask-httpauth.readthedocs.io/en/latest/" target="_blank">`Flask-HTTPAuth`</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resources

**Read or watch:**

- <a href="https://www.youtube.com/watch?v=501dpx2IjGY" target="_blank">REST API Authentication Mechanisms - Only the session auth part</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie" target="_blank">HTTP Cookie</a>
- <a href="https://palletsprojects.com/p/flask/" target="_blank">Flask</a>
- <a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies" target="_blank">Flask Cookie</a>

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

### Requirements

**Python Scripts**

- All your files will be interpreted/compiled on `Ubuntu 18.04 LTS` using `python3 (version 3.7)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle style (version 2.5)`
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

---

Dukeson Ehigboria
