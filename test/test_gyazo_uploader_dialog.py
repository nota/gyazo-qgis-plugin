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
from qgis.PyQt.QtWidgets import QApplication
from qgis.PyQt.QtTest import QTest
import sys

class GyazoUploaderDialogTest(unittest.TestCase):
    """Test dialog works."""

    def setUp(self):
        """Runs before each test."""
        self.app = QApplication.instance()
        if not self.app:
            self.app = QApplication(sys.argv)

    def tearDown(self):
        """Runs after each test."""
        if self.app:
            self.app.quit()

    def test_dummy(self):
        """Placeholder test."""
        self.assertTrue(True)

    def test_init_dialog(self):
        """Test minimal dialog initialization."""
        from gyazo_uploader_dialog import GyazoUploaderDialog
        
        # Create dialog with no QGIS interface in testing mode
        dialog = GyazoUploaderDialog(iface=None, testing=True)
        
        # Basic checks
        self.assertIsNotNone(dialog)
        self.assertEqual(dialog.windowTitle(), "Gyazo Uploader")

if __name__ == "__main__":
    unittest.main()

