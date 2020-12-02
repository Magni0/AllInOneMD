from models.Images import DocImage
from main import db
from schemas.ImageSchema import doc_image_schema
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
img = Blueprint('image', __name__, url_prefix='/document/image')