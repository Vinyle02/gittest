# Automated Reordering System
# Automatic purchase orders based on inventory levels

class AutoReorderEngine:
    def __init__(self):
        self.reorder_points = {}
        self.pending_orders = []
        self.min_stock_threshold = 10

    def set_reorder_point(self, sku, reorder_quantity):
        self.reorder_points[sku] = reorder_quantity

    def check_and_create_orders(self, current_inventory):
        new_orders = []
        for sku, level in current_inventory.items():
            reorder_qty = self.reorder_points.get(sku, 50)
            if level <= self.min_stock_threshold:
                order = {
                    "sku": sku,
                    "quantity": reorder_qty,
                    "status": "pending",
                    "auto_generated": True
                }
                new_orders.append(order)
                self.pending_orders.append(order)
        return new_orders

    def submit_orders(self):
        submitted = [o for o in self.pending_orders if o["status"] == "pending"]
        for order in submitted:
            order["status"] = "submitted"
        return len(submitted)
