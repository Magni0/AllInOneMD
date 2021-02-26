from models.Document import Document
from models.Authentication import User
from main import db
from schemas.DocSchema import doc_schema, docs_schema
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_login import login_required, current_user

md = Blueprint('document', __name__, url_prefix="/document")

@md.route("/", methods=["GET"])
@login_required
def doc_index():
    
    """reterive all md documents from database (not files)"""

    docs = Document.query.filter_by(user_id=current_user.get_id())
    return render_template("doc-index.html", docs=docs)
    # docs = Document.query.all()
    # return jsonify(docs_schema.dump(docs))

@md.route("/", methods=["POST"])
@login_required
def doc_create():
    
    """create new md file"""

    pass
    # doc_fields = doc_schema.load(request.json)

    # new_doc = Document()
    # new_doc.docname = doc_fields["docname"]

    # user.documents.append(new_doc)
    
    # db.session.add(new_doc)
    # db.session.commit()
    
    # return jsonify(doc_schema.dump(new_doc))

@md.route("/<int:id>", methods=["GET"])
@login_required
def doc_retrive(id):
    
    """get md file"""

    pass
    # doc = Document.query.get(id)
    # return jsonify(doc_schema.dump(doc))

# @md.route("/<int:id>", methods=["PUT", "PATCH"])
# @login_required
# def doc_update(id):

#     """update a document"""

#     pass
#     # doc_fields = doc_schema.load(request.json)
    
#     # docs = Document.query.filter_by(id=id, user_id=user.id)
    
#     # if docs.count() != 1:
#     #     return abort(401, description="Unauthorized to update this document")

#     # docs.update(doc_fields)
#     # db.session.commit()

#     # return jsonify(doc_schema.dump(docs[0]))

@md.route("/<int:id>", methods=["DELETE"])
@login_required
def doc_delete(id):
    
    """delete a md file"""

    pass
    # doc = Document.query.get(id)
    
    # if not doc:
    #     return abort(400)
    
    # db.session.delete(doc)
    # db.session.commit()

    # return jsonify(doc_schema.dump(doc))

