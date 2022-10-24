import Property;

class Flat(Property):
    def __init__(self, floor, area, rooms, price, address):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Flat: {self.floor}, {self.area} {self.rooms} {self.price} {self.address}'