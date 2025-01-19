# Development Guide

This guide provides instructions for setting up the development environment and running tests for the QGIS Gyazo Uploader plugin on Ubuntu.

## Prerequisites

1. Ubuntu System Requirements:
   - Ubuntu 22.04 LTS or later
   - Python 3.x
   - QGIS 3.0 or later

2. Install system dependencies:
   ```bash
   sudo apt update
   sudo apt install -y python3-qgis qgis python3-pip
   ```

## Environment Setup

1. Set up QGIS environment variables:
   ```bash
   export QGIS_PREFIX_PATH=/usr
   export PYTHONPATH=/usr/share/qgis/python:/usr/share/qgis/python/plugins:$PYTHONPATH
   ```

   Tip: Add these to your `~/.bashrc` for persistence.

2. Clone the repository:
   ```bash
   git clone https://github.com/yuiseki/qgis_gyazo_uploader.git
   cd qgis_gyazo_uploader
   ```

3. Install Python dependencies:
   ```bash
   pip install python-dotenv
   ```

## Running Tests

1. Verify QGIS environment:
   ```bash
   python3 test/verify_qgis.py
   ```
   This script checks if QGIS bindings are properly installed and accessible.

2. Run all tests:
   ```bash
   python -m unittest discover test -v
   ```

3. Run specific test files:
   ```bash
   # Run QGIS environment tests
   python -m unittest test.test_qgis_environment -v
   
   # Run dialog tests
   python -m unittest test.test_gyazo_uploader_dialog -v
   
   # Run translation tests
   python -m unittest test.test_translations -v
   ```

## Test Structure

The test suite includes:
- `test_qgis_environment.py`: Tests QGIS providers and projections
- `test_gyazo_uploader_dialog.py`: Basic UI tests
- `test_translations.py`: Translation functionality tests
- `test_resources.py`: Resource loading tests

## Common Issues

1. "QApplication not initialized" error:
   - Ensure PyQt5 is properly installed with QGIS
   - The test framework initializes QApplication automatically

2. "postgres provider not available" warning:
   - This is optional and won't affect core functionality
   - Install `postgresql` package if needed

3. "Application path not initialized" warnings:
   - These warnings during projection tests are expected
   - Tests will still pass despite these warnings

## Development Workflow

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Run tests before and after making changes:
   ```bash
   python -m unittest discover test -v
   ```

3. Create a pull request with your changes

## Notes

- The test environment uses a headless QApplication for UI tests
- Test data (e.g., `tenbytenraster.asc`) is included in the test directory
- Some tests may be skipped if environment setup is incomplete
