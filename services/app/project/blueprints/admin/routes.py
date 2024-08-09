from flask import Blueprint, render_template, request, redirect, url_for
from functools import wraps
import project.database.admin as admin
from project.database.model import UserTier

from project.blueprints.auth.routes import login_required


from flask_login import current_user

# Defining a blueprint
admin_bp = Blueprint(
    "admin_bp", __name__, template_folder="templates", static_folder="static"
)


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user is None:
            return redirect(url_for("auth_bp.login", next=request.url))
        elif current_user.tier != UserTier.admin:
            # TODO: Create Home Page to redirect for
            return redirect(url_for("auth_bp.index", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


# eventually have an index with dashboard w many tables

# Take actions for users - suspend, bulk suspend
# see how many lists
# see top words across users


@admin_bp.route("/")
@login_required
@admin_required
def dashboard():
    users = admin.get_all_users()
    return render_template("admin.html", title="Admin Dashboard", users=users)
