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
from unittest.mock import patch, MagicMock
from qgis.PyQt.QtWidgets import QApplication, QPushButton
from qgis.PyQt.QtTest import QTest
from qgis.PyQt.QtCore import QBuffer, QIODevice, Qt, QUrl
from qgis.PyQt.QtGui import QImage, QColor
from qgis.PyQt.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
import sys
import json

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

    @patch('gyazo_uploader_dialog.QNetworkAccessManager')
    @patch('gyazo_uploader_dialog.GyazoUploaderDialog.oauth_access_token')
    @patch('gyazo_uploader_dialog.GyazoUploaderDialog.get_image_png_with_attributions')
    def test_upload_to_gyazo(self, mock_get_image, mock_oauth, mock_network_manager):
        """Test Gyazo upload functionality."""
        from gyazo_uploader_dialog import GyazoUploaderDialog
        
        # Mock OAuth token
        mock_oauth.return_value = "test_token"
        
        # Create test image data
        test_image = QImage(100, 100, QImage.Format_RGB32)
        test_image.fill(QColor(255, 255, 255))
        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        test_image.save(buffer, "PNG")
        mock_png_data = buffer.data().data()
        mock_get_image.return_value = mock_png_data
        
        # Create mock network reply
        mock_reply = MagicMock()
        mock_reply.error.return_value = False
        mock_reply.readAll.return_value.data.return_value = json.dumps({
            'permalink_url': 'https://gyazo.com/test123'
        }).encode()
        
        # Set up network manager mock
        mock_manager_instance = MagicMock()
        mock_manager_instance.post.return_value = mock_reply
        mock_network_manager.return_value = mock_manager_instance
        
        # Create dialog and trigger upload
        dialog = GyazoUploaderDialog(iface=None)
        dialog.upload_to_gyazo("test_token")
        
        # Verify network request
        self.assertTrue(mock_manager_instance.post.called)
        call_args = mock_manager_instance.post.call_args
        request = call_args[0][0]  # First argument of first call
        
        # Verify request URL and headers
        self.assertEqual(request.url().toString(), 'https://upload.gyazo.com/api/upload')
        self.assertTrue('multipart/form-data' in request.header(QNetworkRequest.ContentTypeHeader))
        
        # Verify request body contains required parts
        body = call_args[0][1].data()  # Second argument of first call
        body_str = body.decode('utf-8', errors='ignore')
        self.assertIn('Content-Disposition: form-data; name="imagedata"', body_str)
        self.assertIn('Content-Disposition: form-data; name="access_token"', body_str)
        self.assertIn('test_token', body_str)
        self.assertIn('Gyazo for QGIS', body_str)

if __name__ == "__main__":
    unittest.main()

