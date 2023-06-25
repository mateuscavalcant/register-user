from flask import request
from src.model.model_db_user import User
import bcrypt
import time

MAX_LOGIN_ATTEMPTS = 5  
LOCKOUT_PERIOD = 60  


failed_login_attempts = {}

def loginUser():
    def get_failed_login_attempts(email):
        return failed_login_attempts.get(email, 0)

    def increment_failed_login_attempts(email):
        failed_login_attempts[email] = get_failed_login_attempts(email) + 1

    def reset_failed_login_attempts(email):
        failed_login_attempts[email] = 0

    def lock_user(email):
        failed_login_attempts[email] = -1
        unlock_time = time.time() + LOCKOUT_PERIOD
        failed_login_attempts['unlock_time'] = unlock_time

    def is_user_locked():
        unlock_time = failed_login_attempts.get('unlock_time', 0)
        if unlock_time > time.time():
            return True
        return False

    email = request.form["email"]
    password = request.form["password"]

    if is_user_locked(email):
        return "Too many failed login attempts. Please try again later."

    user = User.query.filter_by(email=email).first()

    if user is None or not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        increment_failed_login_attempts(email) 
        if get_failed_login_attempts(email) >= MAX_LOGIN_ATTEMPTS:
            lock_user(email) 
            return "Too many failed login attempts. Your account has been temporarily locked."
        else:
            return "Incorrect email or password"
    else:
        reset_failed_login_attempts(email) 
        return "Successful Login"
