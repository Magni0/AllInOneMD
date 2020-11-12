from flask import Flask, request, jsonify
app = Flask(__name__)

from database import init_db
db = init_db(app)

from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

from controllers import registable_controllers

for controller in registable_controllers:
    app.register_blueprint(controller)