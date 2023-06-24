from src.model.model_db_user import db, User

def initializeDB(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def insertUser(name, lastname, email, password):
    user = User(name=name, lastname=lastname, email=email, password=password)
    db.session.add(user)
    db.session.commit()


def existEmail(email):
    return User.query.filter_by(email=email).first() is not None
