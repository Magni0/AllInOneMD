from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()

def create_app():

    """This is the main function that works off of the contoller modules, model modules
    and Schema modules. When running the application, run it from this module.
    """

    # init flask with the config setting from default_settings.py 
    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")

    # if the enviroment is production: log errors in logs dir
    if app.config["ENV"] == "production":
        from log_handler import file_handler
        app.logger.addHandler(file_handler)

    # init flask extentions in flask app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from models.Authentication import get_user
    @login_manager.user_loader
    def load_user(user_id):
        return get_user(user_id)

    # imports Blueprint from commands.py to allow custom flask commands
    # custom commands are written in commands.py
    from commands import db_commands
    app.register_blueprint(db_commands)

    # cycles through __init__.py in controllers dir to register Blueprints to flask app
    from controllers import registable_controllers
    for controller in registable_controllers:
        app.register_blueprint(controller)

    # handles validation errors
    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)

    # handles other server errors
    @app.errorhandler(500)
    def handle_500(error):
        app.logger.error(error)
        return ("", 500)

    return app
