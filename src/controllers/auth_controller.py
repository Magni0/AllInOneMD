from models.Authentication import User
from schemas.UserSchema import user_schema
from flask import Blueprint, request, jsonify, abort, redirect, render_template, url_for
from main import db, bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint("auth", __name__, url_prefix="/")

@auth.route("/auth/register", methods=["POST"])
def auth_register():
    # user_fields = user_schema.load(request.json)
    username = request.form.get("username")
    password = request.form.get("password")

    # checks if user already exists
    user = User.query.filter_by(username=username).first()
    if user:
        return abort(400, description="username already taken")

    user = User()
    # user.username = user_fields["username"]
    user.username = username
    # user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    # return jsonify(user_schema.dump(user))
    return redirect(url_for("auth.auth_login"))

@auth.route("/auth/login", methods=["GET"])
def auth_login():
    # user_fields = user_schema.load(request.json)
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort(401, description="Incorrect username or password")
    
    login_user(user)
    # access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))

    # return jsonify({"token": access_token})
    return redirect(url_for("md.doc_index"))

@auth.route("/signout", methods=["GET"])
@login_required
def signout():
    logout_user()
    return redirect("home.html")

@auth.route("/signup", methods=["POST"])
def signup():
    return render_template("signup.html")

@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html")