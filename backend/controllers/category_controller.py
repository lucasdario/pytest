from backend.dao.category_dao import CategoryDao
from backend.controllers.base_controller import BaseController


class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao)
