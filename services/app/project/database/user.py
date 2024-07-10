from model import User
from sqlalchemy import or_

def get_user(username='', email=''):
    user = User.query.filter(or_(User.username==username, User.email==email)).first()
    return user

def normalize_username(raw_username):
    return raw_username.lower().strip()

def normalize_email(raw_email):
    return raw_email.lower().strip()

def validate_email(email):
    errors = []
    if email == '':
        errors.append("Email cannot be empty")
    
    return errors

    