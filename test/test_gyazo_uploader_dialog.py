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
        # Get the QGIS interface mock
        self.dialog = GyazoUploaderDialog(self.iface)

    def tearDown(self):
        """Runs after each test."""
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

