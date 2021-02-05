from flask import Flask, render_template
from front.category import category

app = Flask(__name__)
app.register_blueprint(category)


@app.route('/')
def index():
    return render_template('index.html', title='Best Categories')
