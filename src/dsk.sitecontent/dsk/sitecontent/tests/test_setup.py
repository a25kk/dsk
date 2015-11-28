# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dsk.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dsk.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dsk.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dsk.sitecontent'))

    def test_uninstall(self):
        """Test if dsk.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['dsk.sitecontent'])
        self.assertFalse(self.installer.isProductInstalled('dsk.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDskSitecontentLayer is registered."""
        from dsk.sitecontent.interfaces import IDskSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(IDskSitecontentLayer in utils.registered_layers())
