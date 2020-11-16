from flask import Flask
app = Flask(__name__)
app.config.from_object("default_settings")

from database import init_db
db = init_db(app)

from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

from controllers import registable_controllers
# for controller in registable_controllers:
#     app.register_blueprint(controller)