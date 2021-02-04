import pytest
import sys
sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from backend.dao.category_dao import CategoryDao
from backend.models.category import Category


class TestCategoryDao:
    @pytest.fixture
    def create_instance(self):
        name = "Name 0"
        description = "Description 0"
        return Category(name, description)

    def test_instance(self):
        category_dao = CategoryDao()
        assert isinstance(category_dao, CategoryDao)

    def test_save(self, create_instance):
        category_saved = CategoryDao().save(create_instance)
        assert category_saved.id_ is not None
        CategoryDao().delete(category_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            CategoryDao().save('random_category')

    def test_read_by_id(self, create_instance):
        category_saved = CategoryDao().save(create_instance)
        category_result = CategoryDao().read_by_id(category_saved.id_)
        assert isinstance(category_result, Category)
        CategoryDao().delete(category_result)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            CategoryDao().read_by_id('random_category.id_')

    def test_read_all(self):
        categories = CategoryDao().read_all()
        assert isinstance(categories, list)

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            CategoryDao().delete('random_category')
