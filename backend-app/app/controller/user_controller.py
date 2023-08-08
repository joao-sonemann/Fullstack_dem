from flask import request
from flask_restx import Resource

from app.util.dto import UserDto
from app.service.user_service import create_user, list_all_user, edit_user, delete_user

api = UserDto.api
_user = UserDto.user

@api.route('/')
class Task(Resource):
    def post(self):
        data = request.json
        return create_user(data)

    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return list_all_user()


@api.route('/<id_user>')
@api.param('id_user', 'id user')
class UserComId(Resource):
    def put(self, id_user):
        data = request.json
        return edit_user(id_user, data)

    def delete(self, id_user):
        return delete_user(id_user)