from flask import Flask
from jinja2 import Environment, PackageLoader
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
environment = Environment(loader=PackageLoader('killtheyak', 'templates'))
