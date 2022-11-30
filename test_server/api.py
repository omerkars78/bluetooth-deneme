import flask
from flask import request, jsonify

# from flask_swagger_ui  import get_swaggerui_blueprint
app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Merhaba Python projesi</h1>'''


# A route to return all of the available entries in our catalog.
@app.route('/api', methods=['GET'])
def api_all():


    # Opening JSON file
    with open("data.json") as file:
        data = file.read()
    return jsonify(data)
app.run()

