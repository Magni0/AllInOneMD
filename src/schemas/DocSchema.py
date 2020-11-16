from main import ma
from models.Document import Document
from marshmallow.validate import Length

class DocSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document
    
    name = ma.String(required=True, validate=Length(min=1))

doc_schema = DocSchema()
docs_schema = DocSchema(many=True)