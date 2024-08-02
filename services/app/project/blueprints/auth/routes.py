import project.database.user as user

import sys

import bcrypt
from flask import Blueprint, session, request, abort, jsonify, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return user.get(user_id)

# Defining a blueprint
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@auth_bp.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@auth_bp.route('/')
def index():
    if current_user:
        return current_user.__dict__
    return 'You are not logged in'


@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password_attempt = request.form.get('password')

        print(username, file=sys.stdout)
        print(password_attempt, file=sys.stdout)

        # u = user.get_user(username=username) get password here
        result = user.get_user_by_username(username)
        print(result, file=sys.stdout)
        if not result:
            # user doesnt exist
            return {'status': 'user doesnt exist'}
        
        saved_pw = user.get_password_by_id(result.id)
        print(f"TYPE: {type(saved_pw)}", file=sys.stdout)
        print(f"VAL: {saved_pw}", file=sys.stdout)


        if _verify_password(password_attempt, saved_pw[0]):
            logged_in_user = result
            logged_in_user.is_authenticated = True
            if login_user(logged_in_user):
                # disrespect redirect in next 
                # https://flask-login.readthedocs.io/en/0.6.3/#login-example
                # https://web.archive.org/web/20120517003641/http://flask.pocoo.org/snippets/62/
                return redirect(url_for('auth_bp.index'))
        else:
            return {'login_status': 'failed attempt'}


@auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        u1 = user.get_user_by_username(username=username)
        u2 = user.get_user_by_username(email=email)
        if u1 is not None:
            abort(400, description="Username taken")
        if u2 is not None:
            abort(400, description="Email already in use")
        
        string_password = _get_password_hash(request.form.get('password'))

        new_user = user.new_user(username, email, string_password)
        session['username'] = new_user.username
    

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.index'))


def _get_password_hash(password) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    string_password = hashed_password.decode('utf8')
    return string_password


def _verify_password(plain_password, hashed_password) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc, hashed_password)