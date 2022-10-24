class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return "Employee: " + "First name: " + self.first_name + " Last name: " + self.last_name + " Hire date: " + self.hire_date + " Birth date: " + self.birth_date + " City: " + self.city + " Street: " + self.street + " Zip code: " + self.zip_code + " Phone: " + self.phone
