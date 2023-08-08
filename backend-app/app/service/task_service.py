from app.model.task_model import Task
from app.extensions import db


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def create_task(data):
    task = Task(
        descrybe=data['descrybe'],
        deadline=data['deadline'],
        id_user=data['id_user'],
    )
    save_changes(task)
    return { "id": task.id }


def list_all_task():
    return Task.query.all()

def edit_task(id, data):
    task = Task.query.get(id)
    task.descrybe = data['descrybe']
    task.deadline = data['deadline']
    task.id_user = data['id_user']
    
    save_changes(task)
    return { "id": task.id }

def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return { "id": task.id }