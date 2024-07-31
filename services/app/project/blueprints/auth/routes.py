import project.database.user as user

import bcrypt
from flask import Blueprint, session, request, abort, jsonify, redirect, url_for
from flask_login import LoginManager

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
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password_attempt = request.form.get('password')

        u = user.get_user(username=username)

        if _verify_password(password_attempt, u.password):
            session['username'] = username
            return redirect(url_for('auth_bp.index'))
        
        else:
            return {'login_status': 'failed attempt'}


@auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        u1 = user.get_user(username=username)
        u2 = user.get_user(email=email)
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
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('active', None)
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