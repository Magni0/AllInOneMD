from main import db
from flask import Blueprint

db_commands = Blueprint("db-c", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Created Tables")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Deleted Tables")

@db_commands.cli.command("seed")
def seed_db():
    from models.Document import Document
    from faker import Faker
    faker = Faker()

    for i in range(20):
        doc = Document()
        doc.name = faker.catch_phrase()
        db.session.add(doc)
    
    db.session.commit()
    print("Seeded Tables")