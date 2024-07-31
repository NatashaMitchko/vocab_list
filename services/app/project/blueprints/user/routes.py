import project.database.user as user

from flask import Blueprint, jsonify

# Defining a blueprint
user_bp = Blueprint(
    'user_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@user_bp.route('', methods=['POST'])
def new_user():
    # request
    return jsonify({'hi': 'you'})


def generate_verification_email():
    pass

@user_bp.route('/<username>')
def get_user_by_username(username):
    u = user.get_user(username=username)
    if not u:
        return jsonify({})
    return jsonify({'id': u.id, 'username': u.username, 'email': u.email})

def normalize():
    pass
