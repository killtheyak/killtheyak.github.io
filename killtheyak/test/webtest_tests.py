from unittest import TestCase
from webtest import TestApp
from nose.tools import *
from flask import url_for

from ..main import app

class TestAUser(TestCase):
    def setUp(self):
        app.config['FLATPAGES_ROOT'] = "test/test_pages"
        self.app = TestApp(app)

    def tearDown(self):
        pass

    def test_can_see_homepage(self):
        # Goes to homepage
        res = self.app.get('')
        assert_equal(res.status_code, 200)
        assert_in("All I want to do is", res)

    def test_can_see_a_page(self):
        # Goes to homepage
        res = self.app.get('')
        # Sees titles for a page
        assert_in('install Python', res)
        # Clicks on a title
        res = res.click('install Python')
        # Is at the page
        # Can see the title
        assert_in("Install Python", res)
        # And the OS's
        assert_in("macosx", res)
        # And the content
        assert_in("Verified on MacOSX 10.7.", res)

    def test_can_see_deps(self):
        # Goes to homepage
        res = self.app.get('')
        # Clicks on a page
        res = res.click('install Python')
        # The page has dependency
        # The dependency titles are listed
        assert_in("install-homebrew", res)
        # Clicks on the dependency link (full instructions)
        res = res.click("full instructions")
        # Is at the dependency's page
        assert_in('ruby', res)
