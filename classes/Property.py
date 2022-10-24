class Property():
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    @property
    def area(self):
        return self.area

    @area.setter
    def area(self, value):
        self.area = value
        
    @property
    def rooms(self):
        return self.rooms

    @rooms.setter
    def rooms(self, value):
        self.rooms = value

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        self.price = value
        
    @property
    def address(self):
        return self.address

    @address.setter
    def address(self, value):
        self.address = value