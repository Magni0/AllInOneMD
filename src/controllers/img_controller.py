from models.Images import DocImage
from main import db
from schemas.ImageSchema import doc_image_schema
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from services.decorators import auth_decorator
img = Blueprint('image', __name__, url_prefix='/document/<int:doc_id>/image')

@img.route("/", methods=["POST"])
@jwt_required
@auth_decorator
def doc_create_image(doc_id, user=None):
    pass

@img.route("/<int:id>", methods=["GET"])
@jwt_required
@auth_decorator
def doc_show_image(doc_id, id, user=None):
    pass

@img.route("/<int:id>", methods=["DELETE"])
@jwt_required
@auth_decorator
def doc_delete_image(doc_id, id, user=None):
    pass
