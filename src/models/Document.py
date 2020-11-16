# creates a circular import
from main import db

class Document(db.Model):
    __tablename__="documents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())