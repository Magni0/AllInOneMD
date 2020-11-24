from main import db

class User(db.Model):
    __tablename__="accounts"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    documents = db.relationship("Document", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"