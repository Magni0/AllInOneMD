from main import db

class DocImage(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    imagename = db.Column(db.String())
    doc_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=False)

    def __repr__(self):
        return f"<Image {self.imagename}>"