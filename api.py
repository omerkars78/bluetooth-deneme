# from flask import Flask
# from flask_restful import Resource, Api, reqparse
# import pandas as pd
# import ast
# import json
# import data2 
# app = Flask(__name__)
# api = Api(app)

# class Users(Resource):
#     def get(self):
#         data = pd.read_csv('users.csv')  # read CSV
#         data = data.to_dict()  # convert dataframe to dictionary
#         return {'data': data}, 200  # return data and 200 OK code
#     def post(self):
#         parser = reqparse.RequestParser()  # initialize
#         parser.add_argument('userId', required=True)  # add args
#         parser.add_argument('name', required=True)
#         parser.add_argument('city', required=True)
#         args = parser.parse_args()  # parse arguments to dictionary

#         # read our CSV
#         data = pd.read_csv('users.csv')

#         if args['userId'] in list(data['userId']):
#             return {
#                 'message': f"'{args['userId']}' already exists."
#             }, 409
#         else:
#             # create new dataframe containing new values
#             new_data = pd.DataFrame({
#                 'userId': [args['userId']],
#                 'name': [args['name']],
#                 'city': [args['city']],
#                 'locations': [[]]
#             })
#             # add the newly provided values
#             data = data.append(new_data, ignore_index=True)
#             data.to_csv('users.csv', index=False)  # save back to CSV
#             return {'data': data.to_dict()}, 200  # return data with 200 OK

#     def put(self):
#         parser = reqparse.RequestParser()  # initialize
#         parser.add_argument('userId', required=True)  # add args
#         parser.add_argument('location', required=True)
#         args = parser.parse_args()  # parse arguments to dictionary

#         # read our CSV
#         data = pd.read_csv('users.csv')
        
#         if args['userId'] in list(data['userId']):
#             # evaluate strings of lists to lists !!! never put something like this in prod
#             data['locations'] = data['locations'].apply(
#                 lambda x: ast.literal_eval(x)
#             )
#             # select our user
#             user_data = data[data['userId'] == args['userId']]

#             # update user's locations
#             user_data['locations'] = user_data['locations'].values[0] \
#                 .append(args['location'])
            
#             # save back to CSV
#             data.to_csv('users.csv', index=False)
#             # return data and 200 OK
#             return {'data': data.to_dict()}, 200

#         else:
#             # otherwise the userId does not exist
#             return {
#                 'message': f"'{args['userId']}' user not found."
#             }, 404

#     def delete(self):
#         parser = reqparse.RequestParser()  # initialize
#         parser.add_argument('userId', required=True)  # add userId arg
#         args = parser.parse_args()  # parse arguments to dictionary
        
#         # read our CSV
#         data = pd.read_csv('users.csv')
        
#         if args['userId'] in list(data['userId']):
#             # remove data entry matching given userId
#             data = data[data['userId'] != args['userId']]
            
#             # save back to CSV
#             data.to_csv('users.csv', index=False)
#             # return data and 200 OK
#             return {'data': data.to_dict()}, 200
#         else:
#             # otherwise we return 404 because userId does not exist
#             return {
#                 'message': f"'{args['userId']}' user not found."
#             }, 404

# class Locations(Resource):
#     pass
# api.add_resource(Users, '/users')  # '/users' is our entry point
# api.add_resource(Locations, '/locations')  

# if __name__ == '__main__':
#     app.run()  # run our Flask app

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = False

# Create some test data for our catalog in the form of a list of dictionaries.



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Merhaba Python projesi</h1>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    # Opening JSON file
    with open("data.json") as file:
        data = file.read()
    return jsonify(data)
app.run()

# from flask import Flask, request, jsonify
# from flask_restful import Api, Resource

# app = Flask(__name__)

# api = Api(app)

# class returnjson(Resource):
# 	def get(self):
#         with open("data.json") as file:
#             data = file.read()
#         return jsonify(data)

# api.add_resource(returnjson,'/returnjson')


# if __name__=='__main__':
# 	app.run(debug=True)
