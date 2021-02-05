import sys
sys.path.append('.')
from backend.models.base_model import BaseModel
from sqlalchemy.orm import validates
from sqlalchemy import Column, String


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column(String(length=100))
    description = Column(String(length=255))

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Nome deve estar no formato de texto(String)!")
        if not name.strip():
            raise ValueError("Nome não deve ser vazio!")
        if len(name) > 100:
            raise ValueError("Nome não deve ser maior que 100 caracteres!")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError(
                "Descrição deve estar no formato de texto(String)!")
        if not description.strip():
            raise ValueError("Descrição não deve ser vazio!")
        if len(description) > 255:
            raise ValueError(
                "Descrição não deve ser maior que 255 caracteres!")
        return description
