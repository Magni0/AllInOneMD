from models.Document import Document
from models.Authentication import Authentication
from main import db
from schemas.DocSchema import doc_schema, docs_schema
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
md = Blueprint('document', __name__, url_prefix="/document")

@md.route("/", methods=["GET"])
@jwt_required
def doc_index():
    # retrive all md documents
    user_id = get_jwt_identity()
    user = Authentication.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    docs = Document.query.all()
    return jsonify(docs_schema.dump(docs))

@md.route("/", methods=["POST"])
@jwt_required
def doc_create():
    # create new doc
    doc_fields = doc_schema.load(request.json)
    user_id = get_jwt_identity()
    
    user = Authentication.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    new_doc = Document()
    new_doc.name = doc_fields["name"]

    user.documents.append(new_doc)
    
    db.session.add(new_doc)
    db.session.commit()
    
    return jsonify(doc_schema.dump(new_doc))

@md.route("/<int:id>", methods=["GET"])
@jwt_required
def doc_retrive(id):
    # get single doc
    user_id = get_jwt_identity()
    user = Authentication.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    doc = Document.query.get(id)
    return jsonify(doc_schema.dump(doc))

@md.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
def doc_update(id):
    # update a document
    doc_fields = doc_schema.load(request.json)
    user_id = get_jwt_identity()

    user = Authentication.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")
    
    docs = Document.query.filter_by(id=id, user_id=user.id)
    
    if docs.count() != 1:
        return abort(401, description="Unauthorized to update this document")

    docs.update(doc_fields)
    db.session.commit()

    return jsonify(doc_schema.dump(docs[0]))

@md.route("/<int:id>", methods=["DELETE"])
@jwt_required
def doc_delete(id):
    # delete a document
    user_id = get_jwt_identity()

    user = Authentication.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    doc = Document.query.get(id)
    
    if not doc:
        return abort(400)
    
    db.session.delete(doc)
    db.session.commit()

    return jsonify(doc_schema.dump(doc))