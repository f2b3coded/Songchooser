from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from random import randint

nummer = randint(0, 10000)

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class getClasses(Resource):  # /get
    def get(self):
        # returnt containernummer en een leuke tekst
        return {'container': nummer,
                'text': "Cloud Infra ftw"
                }

api.add_resource(getClasses, '/get')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')