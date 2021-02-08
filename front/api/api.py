from flask import Flask
from flask_restful import Api

from backend.resources.category_resources import CategoryResource

app_api = Flask(__name__)
api = Api(app_api)

api.add_resource(CategoryResource, '/api/category', endpoint='categories')
api.add_resource(CategoryResource, '/api/category/<int:id>',
                 endpoint='category')


@app_api.route('/')
def index():
    return 'Bem Vindo!'
