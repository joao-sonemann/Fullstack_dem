from app.model.user_model import User

def List_user():
    return User.query.all()