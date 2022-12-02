# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
number = int(input("Введите размер списка: \n"))
new_list = []
new_list2 = []
for i in range(number):
    new_list.append(random.randint(-10, 10))
for i in range(len(new_list)):
    while i < len(new_list)/2 and number > len(new_list)/2:
        number = number - 1
        a = new_list[i] * new_list[number]
        new_list2.append(a)
        i += 1
print("Список:\n",new_list)
print("Список из пар чисел:\n",new_list2)