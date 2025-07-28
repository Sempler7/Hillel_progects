def sum_numbers(a, b):
    return a + b
print("\n", sum_numbers(3, 4), "\n")


print()
print()


def calculate_tax(user_income):
    if user_income < 10000:
        tax_amount = user_income * 0.1
    elif user_income < 50000:
        tax_amount = user_income * 0.15
    elif user_income > 500000:
        tax_amount = user_income * 0.20
    return round(tax_amount, 2)
print(calculate_tax(49999), "\n")


print()
print()


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return (self.a + self.b + self.c) / 2

    def perimetr(self):
        return self.a + self.b + self.c

    def format_number(self, num):
        return str(int(num)) if num.is_integer() else f"{num:.2f}"

    def __str__(self):
        area = self.format_number(self.area())
        perimetr = self.format_number(self.perimetr())
        return f"Area: {area}, Perimeter: {perimetr}"

triangle = Triangle(13, 20, 30)

print(triangle)