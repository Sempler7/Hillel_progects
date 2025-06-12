#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

some_symbol = input("Enter some text: ")
unique_chars = set()

for char in some_symbol:
    unique_chars.add(char)

count = len(unique_chars)
if count > 10:
    print("True")
else:
    print("False")
