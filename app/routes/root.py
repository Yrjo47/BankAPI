from flask import Blueprint, render_template

root_routes = Blueprint('root_routes', __name__)


@root_routes.route('/', methods=['GET'])
def get_users_route():
    return render_template('index.html')
