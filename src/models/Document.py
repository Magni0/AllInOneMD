from main import db

class Document(db.Model):
    __tablename__="documents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    
    def __repr__(self):
        return f"<Document {self.name}>"