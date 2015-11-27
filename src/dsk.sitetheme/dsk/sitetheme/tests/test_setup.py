# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dsk.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dsk.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dsk.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dsk.buildout'))

    def test_uninstall(self):
        """Test if dsk.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['dsk.buildout'])
        self.assertFalse(self.installer.isProductInstalled('dsk.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDskBuildoutLayer is registered."""
        from dsk.buildout.interfaces import IDskBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IDskBuildoutLayer in utils.registered_layers())
