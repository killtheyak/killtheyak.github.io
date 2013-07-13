# -*- coding: utf-8 -*-
import os

try:
    # Assumes package is located in the same directory
    # where this file resides
    PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    PACKAGE_DIR = ""


def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(PACKAGE_DIR)
# Necessary for Github pages
FREEZER_BASE_URL = 'http://localhost/killtheyak/'
FREEZER_DESTINATION = PROJECT_ROOT
FREEZER_REMOVE_EXTRA_FILES = False
DEBUG = True
SECRET_KEY = 'shhhh'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'footnotes']
FLATPAGES_ROOT = os.path.join(PROJECT_ROOT, 'killtheyak-pages')
FLATPAGES_EXTENSION = '.md'


# Javascript directory
JAVASCRIPT_DIR = os.path.join(PACKAGE_DIR, 'static', 'js')
# Coffeescript directory
COFFEE_DIR = os.path.join(PACKAGE_DIR, 'static', 'coffee')
