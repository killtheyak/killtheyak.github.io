# -*- coding: utf-8 -*-

"""
Single entry-point that resolves the
import dependencies.

This file is also used to run the app:
    python main.py
"""
import os
from app import app, pages, environment, freezer

from views import *
import filters

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
