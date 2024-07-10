from flask_restful import Resource

class Book(Resource):
    def get(self, ISBN):
        return {'book': f'{ISBN}'}

    def post(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass