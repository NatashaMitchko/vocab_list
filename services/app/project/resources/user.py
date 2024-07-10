import bcrypt
from flask import request
from flask_restful import Resource
from project.database.user import get_user, normalize_username, normalize_email, validate_email


class User(Resource):
    def get(self, user):
        return {'book': f'{user}'}

    def post(self):
        username = normalize_username(request.form.get('username'))
        if username == '':
            return 400 # cant be empty

        email = normalize_email(request.form.get('email'))
        errors = validate_email(email)
        if errors:
            return 400

        get_user(username=username, email=email)

        password = bcrypt.generate_password_hash(request.form.get('password'))




    def delete(self):
        pass

    def update(self):
        pass