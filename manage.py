# -*- coding: utf-8 -*-
'''Management commands.'''

import os
from datetime import datetime
from flask.ext.script import Manager
from flask_frozen import Freezer
from killtheyak.main import app

manager = Manager(app)
freezer = Freezer(app)


@manager.command
def install():
    '''Installs all required packages.'''
    os.system('pip install -U -r requirements.txt')


@manager.command
def coffee(watch=False):
    '''Compiles Coffeescript files.

    To do a one-time compile, run:
        >> ./manage.py coffee

    Enters watch mode when you run:
        >> ./manage.py coffee -w
    '''
    JAVASCRIPT_DIR = app.config['JAVASCRIPT_DIR']
    COFFEE_DIR = app.config['COFFEE_DIR']
    base_command = 'coffee -o {} '.format(JAVASCRIPT_DIR)
    coffee_files = "{}/*.coffee".format(COFFEE_DIR)
    if watch:
        print("Watching .coffee files in {} to {}"
                        .format(COFFEE_DIR, JAVASCRIPT_DIR))
        command = base_command + '-cw ' + coffee_files
    else:
        print("Compiling .coffee files in {} and compiling them to {}"
                        .format(COFFEE_DIR, JAVASCRIPT_DIR))
        command = base_command + '-c ' + coffee_files
    os.system(command)


@manager.command
def build():
    '''Builds the project. Outputs files to build/.'''
    coffee()  # Compile coffeescript
    print("Freezing it up! Brr...")
    freezer.freeze()  # Freezes the project to build/


@manager.command
def deploy(push=True):
    '''Deploys the site.'''
    build()
    os.system('git checkout master')
    os.system("git pull origin master")
    os.system('git submodule update')
    os.system('git checkout -b gh-pages')
    os.system('git merge master')
    os.system('git pull origin gh-pages')
    if push:
        os.system('git push --all')


@manager.command
def test(unit=True, webtest=True):
    """Runs the tests.
    """
    command = 'nosetests --verbosity=2'
    if not unit:
        command += ' --exclude="unit_tests'
    if not webtest:
        command += ' --exclude="webtest_tests"'
    os.system(command)


if __name__ == '__main__':
    manager.run()
