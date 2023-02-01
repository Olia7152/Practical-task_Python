# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество n долек шоколадки: '))
m = int(input('Введите количество m долек шоколадки: '))
k = int(input('Введите количество долек, которое вы хотите отломить: '))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')