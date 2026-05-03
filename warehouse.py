# Warehouse Management System
# Multi-warehouse location tracking for Acme Shoes inventory

class Warehouse:
    def __init__(self, warehouse_id, location):
        self.warehouse_id = warehouse_id
        self.location = location
        self.inventory = {}

    def add_stock(self, sku, quantity):
        self.inventory[sku] = self.inventory.get(sku, 0) + quantity

    def remove_stock(self, sku, quantity):
        if self.inventory.get(sku, 0) >= quantity:
            self.inventory[sku] -= quantity
            return True
        return False

    def get_inventory(self):
        return self.inventory

class WarehouseManager:
    def __init__(self):
        self.warehouses = {}

    def create_warehouse(self, warehouse_id, location):
        self.warehouses[warehouse_id] = Warehouse(warehouse_id, location)

    def get_warehouse(self, warehouse_id):
        return self.warehouses.get(warehouse_id)
