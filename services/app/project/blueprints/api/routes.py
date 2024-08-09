from flask import Blueprint, request
import project.database.user as user

api_bp = Blueprint(
    "api_bp", __name__, template_folder="templates", static_folder="static"
)


@api_bp.route("/email")
def email_taken():
    email = request.args.get("email")
    if user.email_in_use(email):
        return 200, {"available": False}
    return 200, {"available": True}
