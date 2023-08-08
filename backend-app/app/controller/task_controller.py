from flask import request
from flask_restx import Resource

from app.util.dto import TaskDto
from app.service.task_service import create_task, list_all_task, edit_task, delete_task

api = TaskDto.api
_task = TaskDto.task

@api.route('/')
class Task(Resource):
    def post(self):
        data = request.json
        return create_task(data)

    @api.marshal_list_with(_task, envelope='data')
    def get(self):
        return list_all_task()


@api.route('/<id_task>')
@api.param('id_task', 'id task')
class TaskComId(Resource):
    def put(self, id_task):
        data = request.json
        return edit_task(id_task, data)

    def delete(self, id_task):
        return delete_task(id_task)