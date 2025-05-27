# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

single_quotes = 0
for quote in alice_in_wonderland:
    if quote == "'":
        single_quotes += 1
        print(quote)
print(f"Quotes quantity: {single_quotes}\n")

# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_sea_area = black_sea_area + azov_sea_area
print(f"\nThe Black Sea and the Azov Sea together cover an area of {total_sea_area} km²\n")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291
storage1_and_storage2 = 250449
storage2_and_storage3 = 222950

storage1 = total_goods - storage2_and_storage3
storage2 = storage1_and_storage2 - storage1
storage3 = storage2_and_storage3 - storage2

# check
print(f"Total goods: {storage1 + storage2 + storage3}")

print(f"There are {storage1} goods in the first storage")
print(f"There are {storage2} goods in the second storage")
print(f"There are {storage3} goods in the third storage\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month = 18
monthly_payment = 1179
comp_price = monthly_payment * month
print(f"The total cost of the computer will be {comp_price} UAH\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("a) = 8019 % 8 =", 8019 % 8)
print("b) = 9907 % 9 =", 9907 % 9)
print("c) = 2789 % 5 =", 2789 % 5)
print("d) = 7248 % 6 =", 7248 % 6)
print("e) = 7128 % 5 =", 7128 % 5)
print("f) = 19224 % 9 =", 19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_large = 274 * 4
pizza_medium = 218 * 2
juice = 35 * 4
cake = 350
water = 21 * 3
total_order_sum = pizza_large + pizza_medium + juice + cake + water
print(f"Total order cost: {total_order_sum} UAH\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos = 232
photo_per_page = 8
pages = photos // photo_per_page

rem_photo = photos % photo_per_page
if rem_photo > 0:
    pages += 1

print(f"Igor will need {pages} album pages for all the photos\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_per_100km = 9
tank_capacity = 48

total_fuel  = (distance / 100) * fuel_per_100km
refuels = total_fuel // tank_capacity
rem_refuels = total_fuel % tank_capacity
if rem_refuels > 0:
    refuels += 1
print(f"A total of {round(total_fuel)} liters of gasoline will be needed")
print(f"Min refuels {round(refuels)}")
