# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def recursion(a,b):
    if b == 0:
        return 1
    else:
        return a * recursion(a, b - 1)
    
    
a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", recursion(a, b))