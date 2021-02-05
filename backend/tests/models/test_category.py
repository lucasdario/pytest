import sys
sys.path.append('.')
from backend.models.category import Category
from backend.models.base_model import BaseModel
import pytest


@pytest.mark.parametrize("name, description", [
    ("Vegetais", "Gostosinhos e às vezes verdes."),
    ("Cristais", " líquidos discóticos fotoisomerizaveis."),
    ("Frutas", "Coloridas e gostosinhas.")
])
def test_instance_category(name, description):
    category = Category(name, description)
    assert isinstance(category, BaseModel)
    assert isinstance(category, Category)


@pytest.mark.parametrize("name, description", [
    ("", "valid description"),
    ("a" * 200, "valid description"),
    (" ", "valid description")
])
def test_name_not_valid(name, description):
    with pytest.raises(ValueError):
        category = Category(name, description)


@pytest.mark.parametrize("name, description", [
    (10, "valid description"),
    (5.4, "valid description"),
    (True, "valid description")
])
def test_name_format_not_valid(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description)


@pytest.mark.parametrize("name, description", [
    ("valid name", ""),
    ("valid name", "a" * 300),
    ("valid name", " "),
])
def test_description_not_valid(name, description):
    with pytest.raises(ValueError):
        category = Category(name, description)


@pytest.mark.parametrize("name, description", [
    ("valid name", 10),
    ("valid name", 5.3),
    ("valid name", True),
])
def test_name_format_not_valid(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description)
