from flask import Blueprint, render_template
import project.database.user_content as user_content
from flask_login import login_required, current_user

home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/")
def index():
    """
    Main page for logged in & logged out exp
    """
    return render_template("homepage.html")


@home_bp.route("/home")
@login_required
def home():
    # lists
    # books
    # all vocab
    lists = user_content.get_lists_for_user(current_user.id)
    return render_template("user_home.html", title="Home", data={"lists": lists})
