# Inventory Tracking Module
# Real-time inventory level tracking for Acme Shoes

class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def update_stock(self, sku, quantity, operation="add"):
        if operation == "add":
            self.inventory[sku] = self.inventory.get(sku, 0) + quantity
        elif operation == "remove":
            self.inventory[sku] = self.inventory.get(sku, 0) - quantity
        return self.inventory[sku]

    def get_stock_level(self, sku):
        return self.inventory.get(sku, 0)
