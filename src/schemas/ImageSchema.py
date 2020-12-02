from main import ma
from models.Images import DocImage
from schemas.DocSchema import DocSchema
from marshmallow.validate import Length

class DocImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DocImage

        filename = ma.String(required=True, validate=Length(min=1))
        document = ma.Nested(DocSchema)

doc_image_schema = DocImageSchema()