from flask import render_template, Blueprint, request
from werkzeug.utils import redirect
from backend.controllers.category_controller import CategoryController
from backend.models.category import Category
category = Blueprint(__name__, 'category')


@category.route('/category/list')
def index():
    list_category = CategoryController().read_all()
    return render_template('category/list.html', title='Best Categories', category=list_category)


@category.route('/category/create', methods=['GET'])
def form():
    return render_template('category/create.html', title='Best Categories')


@category.route('/category/create', methods=['POST'])
def create():
    id_ = request.form.get('id')
    name_ = request.form.get('name')
    description_ = request.form.get('description')

    if id_:
        obj = CategoryController().read_by_id(int(id_))
        obj.name = name_
        obj.description = description_
        CategoryController().update(obj)
        return redirect('list')

    CategoryController().create(Category(name_, description_))

    return redirect('list')


@category.route('/category/update', methods=['GET'])
def update():
    id_ = request.args.get('cod')

    if not id_:
        return render_template('category/create.html', title='Best Categories')

    obj_ = CategoryController().read_by_id(int(id_))
    return render_template('category/update.html', title='Best Categories', obj=obj_)


@category.route('/category/delete', methods=['GET'])
def delete():
    id_ = request.args.get('cod')

    if not id_:
        return redirect('list')

    obj_ = CategoryController().read_by_id(int(id_))
    CategoryController().delete(obj_)
    return redirect('list')
