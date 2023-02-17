# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


data = [int(x) for x in input("Введите значения массива: ").split()]
limits = [int(x) for x in input("Введите минимум и максимум диапазона: ").split()]

result = []
for i in range(len(data)):
    if limits[0] <= data[i] <= limits[1]:
        result.append(i)
print(result)