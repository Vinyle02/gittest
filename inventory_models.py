# Acme Shoes Inventory Management System
# Database models for inventory tracking

class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

class InventoryItem:
    def __init__(self, product_id, quantity, location):
        self.product_id = product_id
        self.quantity = quantity
        self.location = location
