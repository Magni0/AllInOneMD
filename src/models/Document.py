from main import db
# from models.Images import DocImage

class Document(db.Model):
    __tablename__="documents"

    id = db.Column(db.Integer, primary_key=True)
    docname = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    # doc_images = db.relationship("DocImage", backref="document", lazy="dynamic")

    def __repr__(self):
        return f"<Document {self.name}>"
