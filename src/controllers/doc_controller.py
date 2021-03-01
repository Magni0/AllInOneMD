from models.Document import Document
from models.Authentication import User
from main import db
from schemas.DocSchema import doc_schema, docs_schema
from flask import Blueprint, request, render_template, redirect, url_for, abort
from flask_login import login_required, current_user
import os

md = Blueprint('document', __name__, url_prefix="/document")

@md.route("/index", methods=["GET"])
@login_required
def doc_index():
    
    """reterive all md documents from database (not files)"""

    docs = Document.query.filter_by(user_id=current_user.get_id())
    return render_template("doc-index.html", docs=docs)

@md.route("/create", methods=["POST"])
@login_required
def doc_create():
    
    """create new md file"""

    file_name = request.form.get("file_name")

    # exeption wont work with s3 bucket need to refactor
    # Creates new file in temp_file_storage dir with name from template
    try:
        with open(f"temp_file_storage/{file_name}.md", "x"):
            pass
    except FileExistsError:
        return abort(400, description="File already exists")

    # need to send file to s3 bucket here

    # creates a new record with the file name and the current user id
    document = Document()
    document.docname = file_name
    document.user_id = current_user.get_id()

    db.session.add(document)
    db.session.commit()

    return render_template("doc-edit.html", file_name=file_name)

@md.route("/edit/<int:id>", methods=["GET"])
@login_required
def doc_edit(id):
    
    """get md file to edit"""

    pass
    # return render_template("doc-edit.html", content=content)

@md.route("/delete/<int:id>", methods=["GET"])
@login_required
def doc_delete(id):
    
    """delete a md file"""

    document = Document.query.filter_by(id=id).first()
    print(document)

    # removes file need to update it when implement s3 bucket
    try:
        os.remove(f"temp_file_storage/{document.docname}.md")
        print(f"removed {document.docname}")
    except FileNotFoundError:
        abort(500, description="file not in temp_file_storage")

    # removes db record
    # doc_record = Document.query.filter_by(docname=document.docname, user_id=current_user.get_id())
    # db.session.delete(doc_record)
    db.session.delete(document)
    db.session.commit()

    return redirect(url_for("document.doc_index"))

@md.route("/discard", methods=["GET"])
@login_required
def doc_discard():
    
    """opens an md file to edit"""

    pass

@md.route("/save", methods=["POST"])
@login_required
def doc_save():

    """updates file in s3 bucket"""

    pass

@md.route("/convert/<int:id>", methods=["GET"])
@login_required
def doc_convert(id):

    """converts an md to pdf and downloads it to client"""

    pass 