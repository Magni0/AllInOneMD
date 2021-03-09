import os
import boto3
from main import db
from flask import Blueprint, request, render_template, redirect, url_for, send_file, after_this_request
from flask_login import login_required, current_user
from models.Document import Document

md = Blueprint('document', __name__, url_prefix="/document")

@md.route("/index", methods=["GET"])
@login_required
def doc_index():
    
    """reterive all md documents from database (not files)"""

    docs = Document.query.filter_by(user_id=current_user.get_id()).all()

    return render_template("doc-index.html", docs=docs)

@md.route("/create", methods=["POST"])
@login_required
def doc_create():
    
    """create new md file"""

    file_name = request.form.get("file_name")

    file_name = file_name.replace(" ", "_")

    # Creates new file in tmp dir with name from template
    with open(f"tmp/{file_name}-{current_user.get_id()}.md", "x"):
        pass

    # connect to s3 bucket
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    # upload file to s3 bucket
    s3.upload_file(f"tmp/{file_name}-{current_user.get_id()}.md", os.environ.get("AWS_S3_BUCKET"), f"{file_name}.md")

    # creates a new record with the file name and the current user id
    document = Document()
    document.docname = file_name
    document.user_id = current_user.get_id()

    db.session.add(document)
    db.session.commit()

    document_id = Document.query.filter_by(docname=file_name, user_id=current_user.get_id()).first()

    file_name.replace("_", " ")

    return render_template("doc-edit.html", file_name=file_name, doc_id=document_id.id)

@md.route("/edit/<int:id>", methods=["GET"])
@login_required
def doc_edit(id):
    
    """get md file to edit"""

    # connect to s3 bucket
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    document = Document.query.filter_by(id=id).first()

    # place code to get file from s3 bucket here or load file from tmp
    try:
        # opens and reads contents in file in tmp
        with open(f"tmp/{document.docname}-{current_user.get_id()}.md", "r") as file:
            content = file.read()
    except FileNotFoundError:
        s3.download_file(os.environ.get("AWS_S3_BUCKET"), f"{document.docname}.md", f"tmp/{document.docname}-{current_user.get_id()}.md")
        # opens and reads contents in file in tmp
        with open(f"tmp/{document.docname}-{current_user.get_id()}.md", "r") as file:
            content = file.read()

    file_name = document.docname
    file_name = file_name.replace("_", " ")

    return render_template("doc-edit.html", content=content, file_name=file_name, doc_id=id)

@md.route("/delete/<int:id>", methods=["GET"])
@login_required
def doc_delete(id):
    
    """delete a md file"""

    # connect to s3 bucket
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    document = Document.query.filter_by(id=id).first()

    # delete file form s3 bucket
    s3.delete_object(Bucket=os.environ.get("AWS_S3_BUCKET"), Key=f"{document.docname}.md")

    # # removes file need to update it when implement s3 bucket
    # try:
    #     os.remove(f"tmp/{document.docname}-{current_user.get_id()}.md")
    #     print(f"removed {document.docname}")
    # except FileNotFoundError:
    #     abort(500, description="file not in tmp")

    # removes db record
    db.session.delete(document)
    db.session.commit()

    return redirect(url_for("document.doc_index"))

@md.route("/discard/<int:id>", methods=["GET"])
@login_required
def doc_discard(id):
    
    """discards changes made in the doc-edit template"""

    document = Document.query.filter_by(id=id).first()

    os.remove(f"tmp/{document.docname}-{current_user.get_id()}.md")

    return redirect(url_for("document.doc_index"))

@md.route("/save/<int:id>", methods=["GET", "POST"])
@login_required
def doc_save(id):

    """updates file in s3 bucket"""

    # connect to s3 bucket
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    document = Document.query.filter_by(id=id).first()

    content_to_save = request.args.get("content")

    # get file from s3 bucket
    s3.download_file(os.environ.get("AWS_S3_BUCKET"), f"{document.docname}.md", f"tmp/{document.docname}-{current_user.get_id()}.md")

    with open(f"tmp/{document.docname}-{current_user.get_id()}.md", "w") as file:
        content = file.write(content_to_save)

    # upload file to s3 bucket
    s3.upload_file(f"tmp/{document.docname}-{current_user.get_id()}.md", os.environ.get("AWS_S3_BUCKET"), f"{document.docname}.md")

    #uncomment once s3 bucket implemented
    os.remove(f"tmp/{document.docname}-{current_user.get_id()}.md")

    return redirect(url_for("document.doc_index"))

@md.route("/convert/<int:id>", methods=["GET"])
@login_required
def doc_convert(id):

    """converts an md to pdf and downloads it to client"""

    # connect to s3 bucket
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    document = Document.query.filter_by(id=id).first()

    # get file from s3 bucket
    s3.download_file(os.environ.get("AWS_S3_BUCKET"), f"{document.docname}.md", f"tmp/{document.docname}-{current_user.get_id()}.md")

    # converts md file to pdf
    os.system(f"mdpdf -o tmp/{document.docname}.pdf tmp/{document.docname}-{current_user.get_id()}.md")
    
    os.remove(f"tmp/{document.docname}-{current_user.get_id()}.md")

    return redirect(url_for("document.doc_download", id=document.id))

@md.route("/download/<int:id>", methods=["GET"])
@login_required
def doc_download(id):
    
    document = Document.query.filter_by(id=id).first()

    # PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'temp_file_storage/file.pdf'
    @after_this_request
    def delete_file(response):
        # document = Document.query.filter_by(id=id).first()
        # print(document.docname)
        os.remove(f"tmp/{document.docname}.pdf")
        return response

    file = os.path.abspath(f"tmp/{document.docname}.pdf")

    return send_file(file)
