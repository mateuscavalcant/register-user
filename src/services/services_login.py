from flask import request
from src.model.model_db_user import User
import bcrypt


def loginUser():
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return "Incorrect email or password"
    if user is None or not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return "Incorrect email or password"
    else:
        return "Successful Login"


