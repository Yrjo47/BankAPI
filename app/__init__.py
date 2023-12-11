from app.routes.menuRoute import menu_routes
from app.routes.root import root_routes
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from config import Config  # Import the Config class from your config file

app = Flask(__name__)
app.config.from_object(Config)  # Load configurations from Config class

db = MongoEngine(app)

app.register_blueprint(root_routes)
app.register_blueprint(menu_routes, url_prefix='/menu')

# Enable CORS for all routes
# CORS(app)
