from main import ma
from models.Document import Document

class DocSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document
    
doc_schema = DocSchema()
docs_schema = DocSchema(many=True)