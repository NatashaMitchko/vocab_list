from flask import Blueprint, render_template

import project.database.user as user

# Defining a blueprint
admin_bp = Blueprint(
    "admin_bp", __name__, template_folder="templates", static_folder="static"
)

# Take actions for users - suspend, bulk suspend
# see how many lists
# see top words across users


@admin_bp.route("/users")
def get_users():
    users = user.get_all_users()
    return render_template("users.html", users=users)
