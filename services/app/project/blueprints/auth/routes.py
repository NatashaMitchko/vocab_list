import project.database.user as user

import bcrypt
from flask import Blueprint, session, request, jsonify, redirect, url_for

# Defining a blueprint
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@auth_bp.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password_attempt = request.form.get('password')

        u = user.get_user(username=username)

        sucessful_attempt = bcrypt.checkpw(password_attempt, u.password)

        if sucessful_attempt:
            session['username'] = username
            session['active'] = True

            return redirect(url_for('auth_bp.index'))
        
        else:
            return jsonify({'login_status': 'failed attempt'})

    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')

        salt = bcrypt.gensalt(rounds=21)
        b_password = request.form.get('password').encode('utf-8')
        db_password = bcrypt.hashpw(b_password, salt).decode('utf-8')


        email = request.form.get('email')

@auth_bp.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('active', None)
    return redirect(url_for('auth_bp.index'))
