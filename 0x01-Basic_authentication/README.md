# 0x01. Basic authentication - (Back-end | Authentification)
<p style="width: 300px; height: auto; margin: 5px auto;">
<img src="https://github.com/Sampul-CodeMine/alx-backend-user-data/blob/main/0x01-Basic_authentication/misc/failed_pass.png" alt="You Shall Not Pass" style="width: 250px" align="center"></p>
## Background Context

In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: `Flask-HTTPAuth`). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resources

**Read or watch:**

- <a href="https://www.youtube.com/watch?v=501dpx2IjGY" target="_blank">REST API Authentication Mechanisms</a>
- <a href="https://docs.python.org/3.7/library/base64.html" target="_blank">Base64 in Python **(Older)**</a> | <a href="https://docs.python.org/3.11/library/base64.html" target="_blank">Base64 in Python **(Newer)**</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization" target="_blank">HTTP header Authorization</a>
- <a href="https://palletsprojects.com/p/flask/" target="_blank">Flask</a>
- <a href="https://en.wikipedia.org/wiki/Base64" target="_blank">Base64 - concept</a>

>
> ### Additional Concepts to Know
> - <a href="https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/" target="_blank">Custom Error Pages</a>
> - <a href="https://flask.palletsprojects.com/en/1.1.x/api/#flask.Blueprint.before_request" target="_blank">`before_request`</a>Flask Method
>
> Use the contents in <a href="https://github.com/Sampul-CodeMine/alx-backend-user-data/blob/main/0x01-Basic_authentication/misc/SimpleAPI.zip" target="_blank">this zip folder</a> to start your project.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What authentication means
- What `Base64` is
- How to encode a string in `Base64`
- What Basic authentication means
- How to send the Authorization header

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
