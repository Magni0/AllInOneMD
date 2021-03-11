from main import db
from flask import Blueprint

db_commands = Blueprint("db-c", __name__)

@db_commands.cli.command("create")
def create_db():

    """creates all tables and coloums from models
    """
    db.create_all()
    print("Created Tables")

@db_commands.cli.command("drop")
def drop_db():

    """drops all tables in database
    """

    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Deleted Tables")

@db_commands.cli.command("seed")
def seed_db():

    """give tables in database false data for testing purposes
    """

    from models.Document import Document
    from models.Authentication import User
    from main import bcrypt
    from faker import Faker
    import random
    
    faker = Faker()
    users = []

    for i in range(5):
        user = User()
        user.username = f"testuser{i}"
        user.password = bcrypt.generate_password_hash("testpasswd").decode("utf-8")
        db.session.add(user)
        users.append(user)

    db.session.commit()

    for i in range(20):
        doc = Document()
        doc.docname = faker.catch_phrase()
        doc.user_id = random.choice(users).id
        db.session.add(doc)
    
    db.session.commit()
    print("Seeded Tables")