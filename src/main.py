from flask import Flask, request, jsonify
app = Flask(__name__)

from database import connection, cursor

from controllers import registable_controllers
for controller in registable_controllers:
    app.register_blueprint(controller)