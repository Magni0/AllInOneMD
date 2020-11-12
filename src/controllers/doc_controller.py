from database import cursor, connection
from flask import Blueprint, request, jsonify
md = Blueprint('md', __name__, url_prefix="/md")

@md.route("/", methods=["GET"])
def doc_index():
    # retrive all md documents
    cursor.execute("SELECT * FROM documents")
    docs = cursor.fetchall()
    
    return jsonify(docs)

@md.route("/", methods=["POST"])
def doc_create():
    # create new doc
    sql = "INSERT INTO documents (name) VALUES (%s);"
    cursor.execute(sql, (request.json["name"],))
    connection.commit()

    sql = "SELECT * FROM documents ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    book = cursor.fetchone()
    
    return jsonify(book)

@md.route("/<int:id>", methods=["GET"])
def doc_retrive(id):
    #get single doc
    sql = "SELECT * FROM documents WHERE id = %s;"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    
    return jsonify(book)

@md.route("/<int:id>", methods=["PUT", "PATCH"])
def doc_update(id):
    # update a document
    sql = "UPDATE documents SET name = %s WHERE id = %s;"
    cursor.execute(sql, (request.json["name"], id))
    connection.commit()

    sql = "SELECT * FROM documents WHERE id = %s"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    
    return jsonify(book)

@md.route("/<int:id>", methods=["DELETE"])
def doc_delete(id):
    # delete a document
    sql = "SELECT * FROM documents WHERE id = %s;"
    cursor.execute(sql, (id,))
    doc = cursor.fetchone()
    
    if doc:
        sql = "DELETE FROM documents WHERE id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()
    
    return jsonify(book)