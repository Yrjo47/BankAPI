from flask import request, Blueprint
from app.controllers.menuPositionController import get_all_menu_positions

menu_routes = Blueprint('menu_routes', __name__)


@menu_routes.route('/menu', methods=['GET'])
def get_users_route():
    return get_all_menu_positions()
