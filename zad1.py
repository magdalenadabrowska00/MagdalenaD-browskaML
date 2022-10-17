#SHIFT ENTER -->run

# Zadanie 1

class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def is_passed(self) -> bool:
    avg = sum(self.marks) / len(self.marks)

    if (avg > 50):
      return True
    else:
      return False
      
  def __str__(self):
        return f'Student: {self.name}: {self.marks}'

#def main():

 
# print(Janek.is_passed())
 # print(Klaudia.is_passed())

#main()


# Zadanie 2

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library City: {self.city} Street: {self.street} ZipCode {self.zip_code} OpenHours {self.open_hours} Phone: {self.phone}'


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


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    
    def __str__(self):
        return f'Book: {self.library}, Publication date: {self.publication_date}, Author name: {self.author_name}, Author surname: {self.author_surname}, Number of pages{self.number_of_pages}'


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Employee: {self.employee} Student: {self.student} Books: {str([str(book) for book in self.books])} OrderDate: {self.order_date}'


def main2():
    library1 = Library("Katowice", "Katowicka", "40-850", "8-16", "646838929")
    library2 = Library("Mikołów", "Mikołowska", "42-850", "8-16", "949383929")
    book1 = Book(library1, "2022-01-01", "Magdalena", "Dąbrowska", "60")
    book2 = Book(library2, "2022-01-01", "Mateusz", "Haręża", "40")
    book3 = Book(library1, "2022-01-01", "Przemysław", "Doktór", "200")
    book4 = Book(library2, "2022-01-01", "Maciej", "Duda", "20")
    book5 = Book(library1, "2022-01-01", "Andrzej", "Duda", "100")
    Magda = Student("Magda", [3, 3, 2, 2, 3, 4, 5, 3, 4])
    Przemek = Student("Przemek", [5, 100, 200, 5, 300, 50])
    employee1 = Employee("Mateusz", "Haręża", '2020-09-09', '1997-12-11', 'Katowice', 'Zawadzka', '50-001', "111444999")
    employee2 = Employee("Maciej", "Duda", '2020-09-09', '2001-12-11', 'Ruda Slaska', 'Opolska', '50-001', "222333444")
    employee3 = Employee("Magdalena", "Dabrowska", '2020-09-09', '2001-12-11', 'Katowice', 'Polska', '50-001', "999888777")
    order1 = Order(employee2, Magda, [book1, book2], "2022-10-17")
    order2 = Order(employee1, Przemek, [book1, book3], '2015-03-04')

    print(order1)
    print(order2)


main2()
    
# zadanie 3
   
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


class House(Property):
    def __init__(self, plot, area, rooms, price, address):
        super().__init__(area, rooms, price, address)
        self.plot = plot
        
    def __str__(self):
        return f'House: {self.plot}, {self.area} {self.rooms} {self.price} {self.address}'


class Flat(Property):
    def __init__(self, floor, area, rooms, price, address):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Flat: {self.floor}, {self.area} {self.rooms} {self.price} {self.address}'
    

def main3():
    prop = Property("Kostuchna", 4, 2000, 'Katowice')
    house = House(prop, '3x4')
    flat = Flat(prop, 12)
    print(house)
    print(flat)


main3()