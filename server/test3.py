from flask import request, jsonify


def read():
    with open("data.json") as file:
        data = file.read()
        print(jsonify(data))

read()