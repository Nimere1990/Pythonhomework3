# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
import random as r
import decimal as d

num = int(input('Введите размер списка:\n'))
list_int = [round(r.random() * r.randint(1, 100), 2) for i in range(num)]
dec_list = [list_int[i] % 1 for i in range(num)]
diff = max(dec_list)-min(dec_list)
print(f'{list_int} =>  {round(diff, 2)}')