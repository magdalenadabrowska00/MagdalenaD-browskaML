import Property;

class House(Property):
    def __init__(self, plot, area, rooms, price, address):
        super().__init__(area, rooms, price, address)
        self.plot = plot
        
    def __str__(self):
        return f'House: {self.plot}, {self.area} {self.rooms} {self.price} {self.address}'