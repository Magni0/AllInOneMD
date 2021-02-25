from models.Authentication import User
from schemas.UserSchema import user_schema
from flask import Blueprint, request, jsonify, abort, redirect, render_template, url_for
from main import db, bcrypt
from datetime import timedelta
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["GET"])
def home():
    return render_template("index.html")

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
    user.username = username
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth.login"))

@auth.route("/auth/login", methods=["POST"])
def auth_login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort(401, description="Incorrect username or password")

    if request.form.get("remember"):
        login_user(user, remember=True, duration=timedelta(days=10))
    else:
        login_user(user)

    return redirect(url_for("document.doc_index"))

@auth.route("/signout", methods=["GET"])
@login_required
def signout():
    logout_user()
    return redirect(url_for("auth.home"))

@auth.route("/signup", methods=["GET"])
def signup():
    return render_template("register.html")

@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html")