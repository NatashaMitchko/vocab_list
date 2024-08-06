from flask import Blueprint, jsonify


api_bp = Blueprint(
    "api_bp", __name__, template_folder="templates", static_folder="static"
)


@api_bp.route("/users")
def get_users():
    pass
