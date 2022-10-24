class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library City: {self.city} Street: {self.street} ZipCode {self.zip_code} OpenHours {self.open_hours} Phone: {self.phone}'
