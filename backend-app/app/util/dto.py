from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user info')
    user = api.model('user', {
        'name': fields.String(required=True, description='name user'),
        'function': fields.String(required=True, description='function of user'),
        'id': fields.integer(required=True),
    })

class TaskDto:
    api = Namespace('task', description='task info')
    task = api.model('task', {
        'id': fields.integer(),
        'descrybe': fields.String(required=True, description='task descrition'),
        'deadline': fields.integer(required=True, description='time to do'),
        'id_user': fields.integer()
    })

