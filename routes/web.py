from flask import Blueprint
from controllers.menu_controller import get_all_menu, add_menu, update_menu, delete_menu

web = Blueprint("web", __name__)

# Endpoint API
web.route("/", methods=["GET"])(get_all_menu)
web.route("/menu/insert", methods=["POST"])(add_menu)
web.route("/menu/update/<int:id_menu>", methods=["PUT"])(update_menu)
web.route("/menu/delete/<int:id_menu>", methods=["DELETE"])(delete_menu)

