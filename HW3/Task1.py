# Задача 1.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

# import random

# n = int(input('Введите количество элементов в массиве: '))
# list = [random.randint(1, 5) for i in range(n)]
# print(list)
# lastElementNumber = len(list) - 1
# lastElement = list[lastElementNumber]
# print(f"Последний элемент массива = {lastElement}")
# result = list.count(lastElement)
# print(f"Число {lastElement} встречается в массиве {result} раз")


''''''

n = int(input('Введите количество элементов массива: '))
print('Введите элементы массива: ')
lst = [int(input()) for i in range(n)]
conunt = lst.count(int(input('Определить сколько раз повторялось число: ')))
print(conunt)

