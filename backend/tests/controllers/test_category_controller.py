import pytest
import sys
sys.path.append('.')
from backend.controllers.base_controller import BaseController
from backend.controllers.category_controller import CategoryController
from backend.models.category import Category


@pytest.fixture
def category_controller_instance():
    return CategoryController()


@pytest.fixture
def category_instance():
    name = 'Category 01'
    description = 'Description 01'
    return Category(name, description)


def test_category_controller_instance(category_controller_instance):
    assert isinstance(category_controller_instance, CategoryController)
    assert isinstance(category_controller_instance, BaseController)


def test_create_category(category_instance, category_controller_instance):
    result = category_controller_instance.create(category_instance)
    assert result.id_ is not None
    assert result.name == category_instance.name
    assert result.description == category_instance.description
    category_controller_instance.delete(result)


def test_update_category(category_instance, category_controller_instance):
    created = category_controller_instance.create(category_instance)
    created.name = 'Category 02'
    created.description = 'Description 02'
    result = category_controller_instance.update(created)
    assert result.id_ is not None
    assert result.name == 'Category 02'
    assert result.description == 'Description 02'
    category_controller_instance.delete(result)


def test_read_by_id_should_return_category(category_instance, category_controller_instance):
    created = category_controller_instance.create(category_instance)
    result = category_controller_instance.read_by_id(created.id_)
    assert isinstance(result, Category)
    assert result.name == created.name
    assert result.description == created.description
    category_controller_instance.delete(result)


def test_read_by_id_should_raise_exception(category_controller_instance):
    with pytest.raises(Exception) as exc:
        category_controller_instance.read_by_id(787954641)
        assert str(exc.value) == 'Objeto não está no banco de dados.'


def test_read_all_should_return_list(category_controller_instance):
    result = category_controller_instance.read_all()
    assert isinstance(result, list)


def test_delete_category(category_instance, category_controller_instance):
    created = category_controller_instance.create(category_instance)
    category_controller_instance.delete(created)

    with pytest.raises(Exception) as exc:
        category_controller_instance.read_by_id(created.id_)
        assert str(exc.value) == 'Objeto não está no banco de dados.'
