from flask import request
from src.database.database_user import insertUser
from src.database.database_user import existEmail
from src.validation.validate_user import validateEmail, validatePassword
import bcrypt


def signupUser():
    name = request.form["name"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]

    if not isinstance(name, str) or not isinstance(lastname, str):
        return "Name and lastname must be of type string."
    elif not name or not lastname:
        return "Invalid name. Please try again."

    if not validateEmail(email):
        return "The email address is not in the correct format. Please try again."
    elif existEmail(email):
        return "There is already a user with this email. Try another one."

    if password != confirm_password:
        return "Passwords don't check. Please try again."
    elif not validatePassword(password):
        return "The password must be between 8 and 20 characters long. Please try again."
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    insertUser(name=name, lastname=lastname, email=email, password=hashed_password.decode("utf-8"))
    return "Registration performed successfully."


