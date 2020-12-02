from models.Authentication import User
from flask import abort
from flask_jwt_extended import jwt_required, get_jwt_identity

class Dcorators:
    def auth_decorator(func):
        def wrapper(*args, **kwargs):

            user_id = get_jwt_identity()
            user = User.query.get(user_id)

            if not user:
                return abort(401, description="Invalid user")

            func_value = func(*args, **kwargs):

        return wrapper