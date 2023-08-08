from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user info')
    user = api.model('user', {
        'name': fields.String(required=True),
        'function': fields.String(required=True),
        'id': fields.Integer(),
    })

class TaskDto:
    api = Namespace('task', description='task info')
    task = api.model('task', {
        'id': fields.Integer(),
        'descrybe': fields.String(required=True),
        'deadline': fields.Integer(required=True),
        'id_user': fields.Integer(required=True)
    })

