#!/usr/bin/env python3
import os
import sys
from qgis.core import QgsApplication, QgsProviderRegistry

def check_qgis():
    """Check QGIS installation and print relevant information."""
    print("=== QGIS Environment Check ===")
    print(f"QGIS_PREFIX_PATH: {os.getenv('QGIS_PREFIX_PATH', 'Not set')}")
    print(f"PYTHONPATH: {os.getenv('PYTHONPATH', 'Not set')}")
    
    try:
        # Initialize QGIS Application
        qgs = QgsApplication([], False)
        qgs.initQgis()
        
        print(f"\n=== QGIS Installation Info ===")
        print(f"QGIS Version: {QgsApplication.QGIS_VERSION}")
        
        # Check providers
        registry = QgsProviderRegistry.instance()
        providers = registry.providerList()
        print(f"\n=== Available Providers ===")
        print(", ".join(providers))
        
        qgs.exitQgis()
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = check_qgis()
    sys.exit(0 if success else 1)
