from flask import Flask, request, jsonify
app = Flask(__name__)

from database import connection, cursor

from doc_controller import md
app.register_blueprint(md)