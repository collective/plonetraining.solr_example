# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plonetraining.solr_example.browser.views import FancySearchView
from plonetraining.solr_example.testing import PLONETRAINING_SOLR_EXAMPLE_FUNCTIONAL_TESTING  # noqa
from collective.solr.testing import activateAndReindex
import unittest


class TestSearchView(unittest.TestCase):
    """Test that plonetraining.solr_example is properly installed."""

    layer = PLONETRAINING_SOLR_EXAMPLE_FUNCTIONAL_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ('Manager', ))
        api.content.create(self.portal, 'Document', title='Lorem Ipsum')
        activateAndReindex(self.portal)

    def test_suggest(self):
        """Test if plonetraining.solr_example is installed."""
        request = self.layer['request']
        view = FancySearchView(self.portal, request)
        request.form['SearchableText'] = 'lore'
        self.assertEqual(
            view.suggest(),
            {'url': 'http://nohost?term=lore&SearchableText=lorem', 'word': u'lorem'}
        )
