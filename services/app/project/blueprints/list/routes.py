from flask import Blueprint, render_template, abort
import project.database.user_content as user_content
from flask_login import login_required, current_user

list_bp = Blueprint(
    "list_bp", __name__, template_folder="templates", static_folder="static"
)


@list_bp.route("/<list_id>/")
@login_required
def list_detail(list_id):
    list_detail = user_content.get_list_detail(list_id=list_id)

    if not list_detail:
        abort(404)

    if int(current_user.id) != list_detail.user_id:
       return f"NOT AUTHORIZED: {current_user.id} != {list_detail.user_id}"
    return render_template("list_detail.html", title=list_detail.title, data=list_detail)
    