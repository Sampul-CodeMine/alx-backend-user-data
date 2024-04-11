# 0x00. Personal data - (Back-end | Authentication)

## Resources

**Read or watch:**

- <a href="https://piwik.pro/blog/what-is-pii-personal-data/" target="_blank">What Is PII, non-PII, and Personal Data?</a>
- <a href="https://docs.python.org/3/library/logging.html" target="_blank">logging documentation</a>
- <a href="https://github.com/pyca/bcrypt/" target="_blank">bcrypt package</a>
- <a href="https://www.youtube.com/watch?v=-ARI4Cz-awo" target="_blank">Logging to Files, Setting Levels, and Formatting</a>

**Additional Materials to Read**

- <a href="https://piwik.pro/blog/what-is-pii-personal-data/" target="_blank">What Is PII, non-PII, and personal data?</a>
- <a href="https://www.digitalguardian.com/blog/uncovering-password-habits-are-users-password-security-habits-improving-infographic" target="_blank">Uncovering Password Habits</a>

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Examples of `Personally Identifiable Information (PII)`
- How to implement a log filter that will obfuscate `PII` fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

### Requirements

- All your files will be interpreted/compiled on `Ubuntu 18.04 LTS` using `python3 (version 3.7)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle style (version 2.5)`
- All your files must be `executable`
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be `type annotated`

---

> Click here for the <a href="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2019/11/a2e00974ce6b41460425.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240411%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240411T072514Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bbc4d268790af689dff7f3a39838bc39cef8dbc3962ca7708add30c2b5dae190">user_data.csv</a>

---

Dukeson Ehigboria
