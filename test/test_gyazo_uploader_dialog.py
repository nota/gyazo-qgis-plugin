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
from unittest.mock import patch
from qgis.PyQt.QtWidgets import QApplication
from qgis.PyQt.QtTest import QTest
from qgis.PyQt.QtCore import QBuffer, QIODevice
from qgis.PyQt.QtGui import QImage, QColor
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

    @patch('gyazo_uploader_dialog.GyazoUploaderDialog.get_image_png_with_attributions')
    def test_init_dialog(self, mock_get_image):
        """Test minimal dialog initialization."""
        from gyazo_uploader_dialog import GyazoUploaderDialog
        
        # Create a 100x100 white image
        test_image = QImage(100, 100, QImage.Format_RGB32)
        test_image.fill(QColor(255, 255, 255))
        
        # Convert QImage to PNG bytes
        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        test_image.save(buffer, "PNG")
        mock_png_data = buffer.data().data()
        mock_get_image.return_value = mock_png_data
        
        # Create dialog with no QGIS interface
        dialog = GyazoUploaderDialog(iface=None)
        
        # Basic checks
        self.assertIsNotNone(dialog)
        self.assertEqual(dialog.windowTitle(), "Gyazo Uploader")
        
        # Verify mock was called
        mock_get_image.assert_called_once()

if __name__ == "__main__":
    unittest.main()

