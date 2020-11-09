from flask import Flask
app = Flask(__name__)


@app.route("/md", methods=["GET"])
def doc_index():
    # retrive all md documents
    cursor.execute("SELECT * FROM documents")

@app.route("/md", methods=["POST"])
def doc_create():
    # create new doc
    pass

@app.route("/md/<int:id>", methods=["GET"])
def doc_retrive(id):
    #get single doc
    pass

@app.route("/md/<int:id>", methods=["PUT", "PATCH"])
def doc_update(id):
    # update a document
    pass

@app.route("/md/<int:id>", methods=["DELETE"])
def doc_delete(id):
    # delete a document
    pass