from flask_restful import Resource

class Word(Resource):
    def get(self, word):
        return {'word': f'{word}'}

    def post(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


