from flask import Flask, render_template
from src.services.services_signup import signupUser
from src.services.services_login import loginUser
from src.database.database_user import initializeDB
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["CONEXION_SERVER_DATABASE"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
initializeDB(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    result = loginUser()
    return result

@app.route("/sign_up", methods=["POST"])
def sign_up():

    result = signupUser()
    return result

if __name__ == '__main__':
    app.run(debug=True)