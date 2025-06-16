
def sum_numbers(string):
    try:
        numbers = string.split(',')
        if not all(num.isdigit() for num in numbers):
            raise ValueError  # Викликаємо помилку вручну
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        return "Не можу це зробити!"

# Масив рядків
arr = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# Викликаємо функцію для кожного елемента списку
results = [sum_numbers(string) for string in arr]

print(results)