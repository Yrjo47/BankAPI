from flask import jsonify
from app.models.MenuPosition import MenuPosition


def get_all_menu_positions():
    menu = MenuPosition.objects().to_json()
    if not menu:
        return jsonify({'message': 'No menu items'}), 400
    return jsonify(menu)
