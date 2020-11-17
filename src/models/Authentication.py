from main import db

class Authentication(db.Model):
    __tablename__="accounts"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"