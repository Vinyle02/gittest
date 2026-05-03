# Barcode Scanning Feature
# Integration for barcode scanning in inventory management

import re

class BarcodeScanner:
    def __init__(self):
        self.scanned_items = []

    def scan_barcode(self, barcode):
        # Validate barcode format
        if not re.match(r'^[0-9]{12,14}$', barcode):
            return {"status": "error", "message": "Invalid barcode format"}

        item = {
            "barcode": barcode,
            "timestamp": None,
            "processed": False
        }
        self.scanned_items.append(item)
        return {"status": "success", "barcode": barcode}

    def get_pending_scans(self):
        return [item for item in self.scanned_items if not item["processed"]]
