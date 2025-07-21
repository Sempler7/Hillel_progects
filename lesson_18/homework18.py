# 1. Генератор, який повертає послідовність парних чисел від 0 до N.

def sequence_up_to(n):
    for i in range(n + 1):
        yield i

gen = sequence_up_to(7)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print()
print()
# # #or
# #
# # for number in sequence_up_to(7):
# #     print(number)


# 2. Генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_up_to(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

fib = fibonacci_up_to(100)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


# or

# for number in fibonacci_up_to(50):
#     print(number)
print()
print()

# 3. Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1  # Починаємо з останнього елемента

    def __iter__(self):
        return self  # Ітератор повертає сам себе

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value

numbers = [10, 20, 30, 40]
reverse_iterator = ReverseListIterator(numbers)

print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))

# for item in reverse_iterator:
#     print(item)

print()
print()

# 4. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N

class EvenNumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration

iterator = EvenNumberIterator(22)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# #or
# for number in iterator:
#     print(number)
print()
print()

# 5. Напишіть декоратор, який логує аргументи та результати викликаної функції.

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Виклик функції {func.__name__}")
        print(f"[LOG] Аргументи: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Результат: {result}")
        return result
    return wrapper

@log_call
def multiply(a, b):
    return a * b

multiply(3, 4)

print()
print()

# 6. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Виняток у функції {func.__name__}: {e}")
            return None  # Або можна повернути значення за замовчуванням
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(5, 0))

