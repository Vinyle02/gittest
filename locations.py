# Multi-Location Support
# Support for multiple Acme Shoes store locations

class Location:
    def __init__(self, location_id, name, address):
        self.location_id = location_id
        self.name = name
        self.address = address
        self.inventory = {}

    def update_inventory(self, sku, quantity):
        self.inventory[sku] = quantity

    def get_inventory(self):
        return self.inventory

class LocationManager:
    def __init__(self):
        self.locations = {}

    def add_location(self, location_id, name, address):
        self.locations[location_id] = Location(location_id, name, address)

    def get_stock_across_locations(self, sku):
        total = 0
        for location in self.locations.values():
            total += location.inventory.get(sku, 0)
        return total

    def find_nearest_stock(self, sku, from_location):
        # Logic to find stock in nearby locations
        return {}
