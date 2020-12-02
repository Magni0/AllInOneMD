from models.Document import Document
from models.Authentication import User
from main import db
from schemas.DocSchema import doc_schema, docs_schema
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.decorators import auth_decorator
md = Blueprint('document', __name__, url_prefix="/document")

@md.route("/", methods=["GET"])
@jwt_required
@auth_decorator
def doc_index(user=None):
    # reterive all md documents
    
    docs = Document.query.all()
    return jsonify(docs_schema.dump(docs))

@md.route("/", methods=["POST"])
@jwt_required
@auth_decorator
def doc_create(user=None):
    # create new doc
    doc_fields = doc_schema.load(request.json)

    new_doc = Document()
    new_doc.docname = doc_fields["docname"]

    user.documents.append(new_doc)
    
    db.session.add(new_doc)
    db.session.commit()
    
    return jsonify(doc_schema.dump(new_doc))

@md.route("/<int:id>", methods=["GET"])
@jwt_required
@auth_decorator
def doc_retrive(id, user=None):
    # get single doc

    doc = Document.query.get(id)
    return jsonify(doc_schema.dump(doc))

@md.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@auth_decorator
def doc_update(id, user=None):
    # update a document
    doc_fields = doc_schema.load(request.json)
    
    docs = Document.query.filter_by(id=id, user_id=user.id)
    
    if docs.count() != 1:
        return abort(401, description="Unauthorized to update this document")

    docs.update(doc_fields)
    db.session.commit()

    return jsonify(doc_schema.dump(docs[0]))

@md.route("/<int:id>", methods=["DELETE"])
@jwt_required
@auth_decorator
def doc_delete(id, user=None):
    # delete a document

    doc = Document.query.get(id)
    
    if not doc:
        return abort(400)
    
    db.session.delete(doc)
    db.session.commit()

    return jsonify(doc_schema.dump(doc))