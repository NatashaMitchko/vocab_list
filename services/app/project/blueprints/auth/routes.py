import project.database.user as user

import bcrypt
from flask import Blueprint, session, request, abort, jsonify, redirect, url_for, render_template
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return user.get_user_by_id(user_id)


# Defining a blueprint
auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)


@auth_bp.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@auth_bp.route("/")
def index():
    return render_template("index.html", title="Home", current_user=current_user)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password_attempt = request.form.get("password")

        # u = user.get_user(username=username) get password here
        result = user.get_user_by_username(username)
        if not result:
            # user doesnt exist
            return {"status": "user doesnt exist"}

        saved_pw = user.get_password_by_id(result.id)

        if _verify_password(password_attempt, saved_pw[0]):
            logged_in_user = result
            if login_user(logged_in_user):
                # https://flask-login.readthedocs.io/en/0.6.3/#login-example
                # https://web.archive.org/web/20120517003641/http://flask.pocoo.org/snippets/62/
                # TODO: check if next is safe here
                target = request.args.get('next')
                return redirect(target or url_for("auth_bp.index"))
            return {"hi": "why did this not work??   "}
        else:
            return {"login_status": "failed attempt"}
    return render_template("login.html", title="Login")


@auth_bp.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")

        u1 = user.get_user_by_username(username=username)
        u2 = user.get_user_by_username(email=email)
        if u1 is not None:
            abort(400, description="Username taken")
        if u2 is not None:
            abort(400, description="Email already in use")

        string_password = user.get_password_hash(request.form.get("password"))

        new_user = user.new_user(username, email, string_password)
        session["username"] = new_user.username


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.index"))


def _verify_password(plain_password, hashed_password) -> bool:
    password_byte_enc = plain_password.encode("utf-8")
    hashed_password = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_byte_enc, hashed_password)
