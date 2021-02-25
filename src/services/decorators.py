# from models.Authentication import User
# from functools import wraps
# from flask import abort
# from flask_jwt_extended import get_jwt_identity

#this is only temporary and will be removed once forms are implemented
# def auth_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         user_id = get_jwt_identity()
#         user = User.query.get(user_id)

#         if not user:
#             return abort(401, description="Invalid user")

#         return func(*args, user=user, **kwargs)

#     return wrapper
