from flask import Flask
from flask_restful import  Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'quote': '“ Code is like humor. When you have to explain it, it’s bad.” – Cory House'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
