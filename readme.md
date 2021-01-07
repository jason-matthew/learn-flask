# Overview 

Retain personal notes and examples for Python Flask applications

Subdirectories capture standalone applications

App | Notes 
----|------
[00](./00) | Hello World
[01](./01) | File upload

## Setup 

```bash
virtualenv -p python3 ~/venv/flask
. ~/venv/flask/bin/activate
pip install flask

export FLASK_APP=run.py
export FLASK_ENV=development        # load codechanges without restarting server
flask run
```

## Usage

```bash
curl localhost:5000/
```

## References

* [Flask Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart)
* [Development Server](https://flask.palletsprojects.com/en/1.1.x/server/#server)
* [flask CLI](https://flask.palletsprojects.com/en/1.1.x/cli/)