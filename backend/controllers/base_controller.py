from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel


class BaseController:
    def __init__(self, dao: BaseDao):
        self.__dao = dao

    def create(self, model: BaseModel) -> BaseModel:
        return self.__dao.save(model)

    def read_by_id(self, id_: int) -> BaseModel:
        result = self.__dao.read_by_id(id_)
        if result:
            return result
        raise Exception('Objeto não está no banco de dados.')

    def update(self, model: BaseModel) -> BaseModel:
        return self.__dao.save(model)

    def read_all(self):
        return self.__dao.read_all()

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)
