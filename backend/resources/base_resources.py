from flask import request
from flask_restful import Resource

from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: BaseModel) -> None:
        self.__dao = dao
        self.__model_type = model_type

    def get(self, id_=None):
        if id_:
            return self.__dao.read_by_id(id_)
        return self.__dao.read_all()

    def post(self):
        data = request.json
        item = self.__model_type(**data)
        self.__dao.save(item)
        return item

    def put(self, id):
        data = request.json

        if data['id_'] == id:
            item = self.__dao.read_by_id(id)

            for key, value in data.items():
                setattr(item, key, value)

            return self.__dao.save(item)

        return None

    def delete(self, id):
        item = self.__dao.read_by_id(id)
        self.__dao.delete(item)
        return None
