from main import ma
from models.Document import Document
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length

class DocSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document
    
    docname = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(UserSchema)

doc_schema = DocSchema()
docs_schema = DocSchema(many=True)