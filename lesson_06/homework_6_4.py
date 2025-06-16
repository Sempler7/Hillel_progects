#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst1 = [1, 2, 3, 4, 5, 6, 7]
lst_sum = 0
for item in lst1:
    if item % 2 == 0:
        lst_sum += item
print(lst_sum)
