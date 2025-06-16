# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):

    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier

        if  result > 25:

            break
        print(f"{number} * {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# # task 2
# """  Написати функцію, яка обчислює суму двох чисел.
# """

def sum_numbers(a, b):
    return a + b
print("\n", sum_numbers(3, 4), "\n")


# # task 3
# """  Написати функцію, яка розрахує середнє арифметичне списку чисел.
# """
list_some_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = (sum(list_some_numbers) / len(list_some_numbers))
print(lst2, "\n")

# # task 4
# """  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
# """

def reverse_it (*number):
    return number[::-1]
print(reverse_it(1, 2, 3, 4, 5), "\n")

# # task 5
# """  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
# """

my_list = ["apple", "pear", "banana", "kiwi", "strawberry", "mandarin"]
longest_word = max(my_list, key=len)
print(longest_word, "\n")

# # task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1
#
# # task 7 Вирахувати площу поверхні прямокутника

def calculate_area(l, w):
    value = l * w # Input change here :: Цей рядок слід змінити
    return value
print("\n", calculate_area(0, 0), "\n")

# # task 8
#
def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


print(is_prime_number(7), "\n")

# # task 9 Написати програму, яка розраховує оподаткування на основі річного доходу користувача.
#
# Отримайте річний дохід користувача.
# Ми припускаємо, що користувач ЗАВЖДИ буде вводити нормальне число (≥0)
# На основі введеного доходу розрахуйте податок за такими умовами:
# Якщо дохід менше 10 000 грн, податок складає 10% від доходу.
# Якщо дохід від 10 000 до 50 000 грн, податок складає 15% від доходу.
# Якщо дохід більше 50 000 грн, податок складає 20% від доходу.
# Запишіть результат у змінну tax_amount.

def calculate_tax(user_income):
    if user_income < 10000:
        tax_amount = user_income * 0.1
    elif user_income < 50000:
        tax_amount = user_income * 0.15
    elif user_income > 500000:
        tax_amount = user_income * 0.20

    return round(tax_amount, 2)
print(calculate_tax(49999), "\n")

# # task 10

def solution(x):
    return x[::-1]

print(solution(str((123456789))))

# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# """