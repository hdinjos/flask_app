from src.models.User import User
from src import db
from flask import Blueprint, render_template, request, redirect

bp = Blueprint("user", __name__)


@bp.route("/user")
def index():
    user = User.query.all()
    print(user)
    return render_template("user.html")


@bp.route("/create", methods=["POST", "GET"])
def create():
    if (request.method == "POST"):
        username = request.form["username"]
        email = request.form["email"]
        user_create = User(username, email)
        db.session.add(user_create)
        db.session.commit()
        return redirect("/user")
    return render_template("user_create.html")
