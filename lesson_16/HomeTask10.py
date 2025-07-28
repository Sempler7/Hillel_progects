# # Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# # сторона_а (довжина сторони a).
# # кут_а (кут між сторонами a і b).
# # кут_б (суміжний з кутом кут_а).
# # Необхідно реалізувати наступні вимоги:

# # Значення сторони сторона_а повинно бути більше 0.
# # Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# # Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.

#РОМБ

class Rhombus:
    def __init__(self, a, alpha):
        if a <= 0 or (alpha <= 0 or alpha >= 180):
            raise ValueError("Некоретне значення!")
        else:
            self.a = a
            self.alpha = alpha
            self.beta = 180 - alpha

    def __str__(self):
        return f"Romb with a = {self.a}, alpha = {self.alpha}, beta = {self.beta}."

romb = Rhombus(17, 7)

print(romb)
print()

#ТРЕУГОЛЬНИК

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return (self.a + self.b + self.c) / 2

    def perimetr(self):
        return self.a + self.b + self.c


#    Вариант 1:
#
#     def info(self):
#         return f"Triangle with sides ({self.a}, {self.b}, {self.c}) → Area: {self.area():.2f}, Perimeter: {self.perimetr():.2f}"
#
# triangle = Triangle(13, 20, 30)
#
# print(triangle.info())


    #Вариант 2: целые числа отображаются без десятичной части, а дробные — с ней

    def format_number(self, num):
        return str(int(num)) if num.is_integer() else f"{num:.2f}"

    def __str__(self):
        area = self.format_number(self.area())
        perimetr = self.format_number(self.perimetr())
        return f"Area: {area}, Perimeter: {perimetr}"

triangle = Triangle(13, 20, 30)

print(triangle)

















































#
#
#
# from math import sin, radians
#
#
#
# class Romb:
#     def __init__(self, a, alpha):
#         if a > 0 and alpha>0 and alpha < 180:
#             self.a = a
#             self.alpha = alpha
#         else:
#             raise ValueError("Некоретне значення!")
#
#     def __str__(self):
#         return f"Romb with a = {self.a}, alpha = {self.alpha}, beta = {self.beta}."
#
#     def periment(self):
#         return 4 * self.a
#
#     def __add__(self, other):
#         return ((self.a)**2)*sin(radians(self.alpha)) + ((other.a)**2)*sin(radians(other.alpha))
#
# romb = Romb(10, 60) + Romb(20, 80)
#
# print(romb)
#
#
#
#
#
    














    




















