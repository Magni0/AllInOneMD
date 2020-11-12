from models.Document import Document
from main import db
from schemas.DocSchema import doc_schema, docs_schema
from flask import Blueprint, request, jsonify
md = Blueprint('md', __name__, url_prefix="/md")

@md.route("/", methods=["GET"])
def doc_index():
    # retrive all md documents
    docs = Document.query.all()
    return jsonify(docs_schema.dump(docs))

@md.route("/", methods=["POST"])
def doc_create():
    # create new doc
    doc_fields = doc_schema.load(request.json)

    new_doc = Document()
    new_doc.name = doc_fields["name"]
    
    db.session.add(new_doc)
    db.session.commit()
    
    return jsonify(doc_schema.dump(new_doc))

@md.route("/<int:id>", methods=["GET"])
def doc_retrive(id):
    # get single doc
    doc = Document.query.get(id)
    return jsonify(doc_schema.dump(doc))

@md.route("/<int:id>", methods=["PUT", "PATCH"])
def doc_update(id):
    # update a document
    docs = Document.query.filter_by(id=id)
    doc_fields = doc_schema.load(request.json)
    docs.update(doc_fields)
    db.session.commit()

    return jsonify(doc_schema.dump(docs[0]))

@md.route("/<int:id>", methods=["DELETE"])
def doc_delete(id):
    # delete a document
    doc = Document.query.get(id)
    db.session.delete(doc)
    db.session.commit()

    return jsonify(doc_schema.dump(doc))