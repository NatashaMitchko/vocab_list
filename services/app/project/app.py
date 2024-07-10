from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from project.resources.book import Book
from project.resources.word import Word
from project.resources.user import User

app = Flask(__name__)
app.config.from_object("project.config.Config")

db = SQLAlchemy(app)

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Word, '/word/<string:word>')
api.add_resource(Book, '/book/<string:ISBN>')
api.add_resource(User, '/user/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)