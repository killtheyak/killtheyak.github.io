'''Unit testing'''

from unittest import TestCase
from nose.tools import *

from flask import Markup
from flask_flatpages import FlatPages
from ..main import app, pages
from ..filters import fenced_code, github_urlize, lower_first


class TestPages(TestCase):

    def setUp(self):
        app.config['FLATPAGES_ROOT'] = 'test/test_pages'
        self.pages = FlatPages(app)

    def test_get_fenced_blocks(self):
        page = self.pages.get('install-python3')
        code = fenced_code(page.html)
        assert_not_in('Verified on MacOSX', code)
        assert_in('brew install python3', code)
        assert_in('brew link python3', code)

class TestFilters(TestCase):
    def setUp(self):
        pass

    def test_github_urlize(self):
        url1 = 'http://www.github.com/sloria'
        assert_equal(github_urlize(url1),
            Markup('<a href="{}">sloria</a>'.format(url1)))
        name = 'Steven Loria'
        assert_equal(github_urlize(name), name)

    def test_lower_first(self):
        assert_equal(lower_first('Install Python 3'), 'install Python 3')
