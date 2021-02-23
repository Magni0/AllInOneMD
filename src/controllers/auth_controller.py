from models.Authentication import User
from schemas.UserSchema import user_schema
from flask import Blueprint, request, jsonify, abort, redirect
from main import db, bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)

    # checks if user already exists
    user = User.query.filter_by(username=user_fields["username"]).first()
    if user:
        return abort(400, description="Email already registered")

    user = User()
    user.username = user_fields["username"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))

@auth.route("/login", methods=["GET"])
def auth_login():
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(username=user_fields["username"]).first()

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username or password")
    
    access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))

    return jsonify({"token": access_token})

# @auth.route("/signout", methods=["GET"])
# def auth_signout():
#     logout_user()
#     return redirect()