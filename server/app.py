#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route("/print/<string:username>")
def user(username):
    print (username)
    return f'{username}'

@app.route("/count/<int:integer>")
def count(integer):
    if integer > 100 or integer < 1:
        return "Integer must be between 1 and 100", 400
    return '\n'.join(map(str, range(integer))) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":  # "div" used to represent division
        if num2 == 0:
            return "Cannot divide by zero", 400
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Operation not found", 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)