from app.model.user_model import User
from app.extensions import db


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def create_user(data):
    new_user = User(
        name=data['name'],
        function=data["function"],

    )
    save_changes(new_user)
    return { "id": new_user.id }


def list_all_user():
    return User.query.all()

def edit_user(id, data):
    user = User.query.get(id)
    user.name = data['name']
    user.function=data["function"]
    save_changes(user)
    return { "id": user.id }

def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return { "id": user.id }