# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetraining.solr_example.testing import PLONETRAINING_SOLR_EXAMPLE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetraining.solr_example is properly installed."""

    layer = PLONETRAINING_SOLR_EXAMPLE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetraining.solr_example is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetraining.solr_example'))

    def test_browserlayer(self):
        """Test that IPlonetrainingSolrExampleLayer is registered."""
        from plonetraining.solr_example.interfaces import (
            IPlonetrainingSolrExampleLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonetrainingSolrExampleLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETRAINING_SOLR_EXAMPLE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetraining.solr_example'])

    def test_product_uninstalled(self):
        """Test if plonetraining.solr_example is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetraining.solr_example'))

    def test_browserlayer_removed(self):
        """Test that IPlonetrainingSolrExampleLayer is removed."""
        from plonetraining.solr_example.interfaces import IPlonetrainingSolrExampleLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonetrainingSolrExampleLayer, utils.registered_layers())
