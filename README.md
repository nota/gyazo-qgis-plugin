# QGIS Gyazo Uploader

A QGIS plugin that allows you to capture your current map view and upload it directly to Gyazo, complete with proper attribution information for all visible layers.

## Features

- Capture the current QGIS map view with a single click
- Automatically includes attribution information for all visible layers in the image
- Secure OAuth authentication with Gyazo
- Direct upload to Gyazo from within QGIS
- Preview captured image before upload
- Automatic browser opening to view uploaded image
- Integrates seamlessly with QGIS toolbar

## Installation

1. Download the plugin
2. Install it through QGIS Plugin Manager
3. Configure your Gyazo OAuth credentials in the `.env` file:
   ```
   GYAZO_CLIENT_ID=your_client_id
   GYAZO_CLIENT_SECRET=your_client_secret
   ```

## Usage

1. Click the Gyazo Uploader icon in the QGIS toolbar
2. Review the preview of your map with attributions
3. Click "Upload to Gyazo"
4. Authenticate with Gyazo (first time only)
5. Your browser will automatically open with the uploaded image

## Note

The plugin will automatically add attribution information for all visible layers to the bottom of the captured image, ensuring proper credit is given to data sources.

When uploading identical map views, the Gyazo API will return the same URL for identical image content.

## Requirements

- QGIS 3.0 or later
- Python 3.x
- Active Gyazo account
- Gyazo API credentials

## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

