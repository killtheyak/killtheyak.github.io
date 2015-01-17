'''Unit testing'''

from unittest import TestCase
from nose.tools import *  # noqa
from datetime import datetime

from flask import Markup
from flask_flatpages import FlatPages
from ..main import app
from ..filters import fenced_code, github_urlize, lower_first, datetime_format


class TestPages(TestCase):

    def setUp(self):
        self.pages = FlatPages(app)

    def test_get_fenced_blocks(self):
        page = self.pages.get('install-python')
        code = fenced_code(page.html)
        assert_not_in('Verified on MacOSX', code)
        assert_in('brew install python3', code)

class TestFilters(TestCase):

    def test_github_urlize(self):
        url1 = 'http://www.github.com/sloria'
        assert_equal(github_urlize(url1),
            Markup('<a href="{}">sloria</a>'.format(url1)))
        name = 'Steven Loria'
        assert_equal(github_urlize(name), name)

    def test_lower_first(self):
        assert_equal(lower_first('Install Python 3'), 'install Python 3')

    def test_datetime_format(self):
        d = datetime.strptime("2013-07-08 10:00", "%Y-%m-%d %H:%M")
        assert_equal(datetime_format(d), "07/08/13")
