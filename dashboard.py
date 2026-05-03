# Inventory Dashboard
# Real-time overview of inventory status across all Acme Shoes locations

class InventoryDashboard:
    def __init__(self, inventory_tracker):
        self.tracker = inventory_tracker

    def get_total_inventory(self):
        return sum(self.tracker.inventory.values())

    def get_low_stock_items(self, threshold=10):
        low_stock = {}
        for sku, quantity in self.tracker.inventory.items():
            if quantity < threshold:
                low_stock[sku] = quantity
        return low_stock

    def generate_summary(self):
        return {
            "total_items": self.get_total_inventory(),
            "low_stock": self.get_low_stock_items()
        }
