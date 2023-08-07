from flask import request
from flask_restx import Resource

from app.util.dto import TaskDto
# from app.service.categoria.service import save_new_user, get_all_users, get_a_user

api = TaskDto.api
# _user = UserDto.user

@api.route('/')
class Task(Resource):

    def post(self):
        pass

    def get(self):
        pass


@api.route('/<id_task>')
@api.param('id_task', 'id da task')
class UserComId(Resource):
    def put(self, id_task):
        pass

    def delete(self, id_task):
        pass
