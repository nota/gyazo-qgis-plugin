# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'yuiseki@gmail.com'
__date__ = '2025-01-18'
__copyright__ = 'Copyright 2025, yuiseki'

import unittest
import sys

from qgis.PyQt.QtWidgets import QDialogButtonBox, QDialog, QApplication
from qgis.PyQt.QtGui import QImage, QColor

from gyazo_uploader_dialog import GyazoUploaderDialog
from test.utilities import get_qgis_app

class GyazoUploaderDialogTest(unittest.TestCase):
    """Test dialog works."""

    @classmethod
    def setUpClass(cls):
        """Run before all tests."""
        # Initialize Qt Application first
        if not QApplication.instance():
            cls.app = QApplication(sys.argv)
        # Then initialize QGIS
        cls.qgis_app, cls.canvas, cls.iface, cls.parent = get_qgis_app()

    def setUp(self):
        """Runs before each test."""
        # Create a mock QImage for testing
        self.test_image = QImage(400, 400, QImage.Format_ARGB32)
        self.test_image.fill(QColor(255, 255, 255))
        
        # Patch the get_image method to return our test image
        def mock_get_image(self):
            return self.test_image
            
        # Patch the get_attributions method to return test data
        def mock_get_attributions(self):
            return ["Test Attribution"]
            
        # Store original methods
        self._original_get_image = GyazoUploaderDialog.get_image
        self._original_get_attributions = GyazoUploaderDialog.get_attributions
        
        # Replace with mocks
        GyazoUploaderDialog.get_image = mock_get_image
        GyazoUploaderDialog.get_attributions = mock_get_attributions
        
        # Now create dialog with mock interface
        self.dialog = GyazoUploaderDialog(self.iface)
        
        # Add button box for testing
        self.dialog.button_box = QDialogButtonBox(self.dialog)
        self.dialog.button_box.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )

    def tearDown(self):
        """Runs after each test."""
        # Restore original methods
        GyazoUploaderDialog.get_image = self._original_get_image
        GyazoUploaderDialog.get_attributions = self._original_get_attributions
        self.dialog = None

    def test_dialog_ok(self):
        """Test we can click OK."""

        button = self.dialog.button_box.button(QDialogButtonBox.Ok)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Accepted)

    def test_dialog_cancel(self):
        """Test we can click cancel."""
        button = self.dialog.button_box.button(QDialogButtonBox.Cancel)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Rejected)

if __name__ == "__main__":
    suite = unittest.makeSuite(GyazoUploaderDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

