from flask import request
from flask_restx import Resource

from app.util.dto import UserDto
from app.service.user_service import List_user

api = UserDto.api
# _user = UserDto.user

@api.route('/')
class User(Resource):

    def post(self):
        pass

    def get(self):
        return List_user()
        


@api.route('/<id_user>')
@api.param('id_user', 'id do user')
class UserComId(Resource):
    def put(self, id_user):
        pass

    def delete(self, id_user):
        pass
