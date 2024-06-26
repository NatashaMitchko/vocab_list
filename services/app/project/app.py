from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

db = {}

class Word(Resource):
    def get(self, word_id):
        word = db.get(word_id)
        return {'word': word}
    
    def put(self, word_id):
        db[word_id] = request.form['word']
        return {'word_id': db[word_id]}


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Word, '/word/<word_id>')

if __name__ == '__main__':
    app.run(debug=True)