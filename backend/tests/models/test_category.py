import sys
sys.path.append('.')
from backend.models.base_model import BaseModel
from backend.models.category import Category

NAME_ = "Móveis"
DESCRIPTION_ = "Móveis para interior."


def instance_obj():
    obj = Category(NAME_, DESCRIPTION_)
    return obj


def test_instace_obj():
    obj = instance_obj()
    assert isinstance(obj, BaseModel)
    assert isinstance(obj, Category)


def test_name_null():
    try:
        obj = instance_obj()
        obj.name = None
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, TypeError)


def test_name_empty():
    try:
        obj = instance_obj()
        obj.name = ''
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, ValueError)


def test_name_value_invalid():
    try:
        obj = instance_obj()
        obj.name = ' '
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, ValueError)


def test_name_type_invalid():
    try:
        obj = instance_obj()
        obj.name = 10.50
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, TypeError)


def test_name_length_invalid():
    try:
        obj = instance_obj()
        obj.name = 'TESTE '*100
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, ValueError)


def test_description_null():
    try:
        obj = instance_obj()
        obj.description = None
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, TypeError)


def test_description_empty():
    try:
        obj = instance_obj()
        obj.description = ''
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, ValueError)


def test_description_value_invalid():
    try:
        obj = instance_obj()
        obj.description = ' '
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, ValueError)


def test_description_type_invalid():
    try:
        obj = instance_obj()
        obj.description = 10.50
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, TypeError)


def test_description_lenght_invalid():
    try:
        obj = instance_obj()
        obj.description = 'TESTE '*200
        assert NotImplementedError("Erro não implementado!")
    except Exception as error:
        assert isinstance(error, ValueError)
