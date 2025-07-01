
# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім('я, зарплата, відділ),
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.name = name
        self.salary = salary
        self.programming_language = programming_language

class  TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size



# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
from math import pi

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"Area is {self.area():.2f}, perimeter is {self.perimeter():.4f}."

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side

    def __str__(self):
        return super().__str__() + "This is Square!"

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * (self.__radius) ** 2

    def perimeter(self):
        return 2 * pi * self.__radius

    def __str__(self):
        return super().__str__() + "This is Circle!"

for i in range(3, 7):
    figures = [Square(i), Circle(i)]

    for figure in figures:
        print(figure)

