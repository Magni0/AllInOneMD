from main import ma
from models.Authentication import Authentication
from marshmallow.validate import Length

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Authentication
        load_only = ["password"]

    username = ma.String(required=True, validate=Length(min=1))
    password = ma.String(required=True, validate=Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)