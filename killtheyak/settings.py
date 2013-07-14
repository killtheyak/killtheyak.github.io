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
FREEZER_DESTINATION = PROJECT_ROOT
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted
FREEZER_DESTINATION_IGNORE = ['*.coffee']
DEBUG = True
SECRET_KEY = 'shhhh'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'footnotes']
FLATPAGES_ROOT = os.path.join(PROJECT_ROOT, 'killtheyak-pages')
FLATPAGES_EXTENSION = '.md'

GITHUB_REPO = "http://www.github.com/killtheyak/killtheyak.github.com"
PAGES_REPO = "http://www.github.com/killtheyak/killtheyak-pages"
RAW_PAGES_PREFIX = "https://raw.github.com/killtheyak/killtheyak-pages/master/"

# Javascript directory
JAVASCRIPT_DIR = os.path.join(PACKAGE_DIR, 'static', 'js')
# Coffeescript directory
COFFEE_DIR = os.path.join(PACKAGE_DIR, 'static', 'coffee')
