# # Задача №2:
# # Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# # Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# # Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# # Пример:
# # 4 4 -> 2 2
# # 5 6 -> 2

# from random import randint

# firstNum = randint(0, 1001) 
# secondNum = randint(0, 1001)
# s = firstNum + secondNum
# p = firstNum * secondNum
# print(f'Загадано два числа.\nСумма этих чисел = {s}.'f'\nПроизведение этих чисел = {p}.\n')

# # S = x + y
# # P = x * y
# # P = (S - y) * y 
# # P = S * y - S**2
# # y**2 - S * y + P = 0

# d = s ** 2 - 4 * p
# secondNum = int(s / 2 + d ** (0.5) / 2)
# firstNum = int(s / 2 - d ** (0.5) / 2)
# print(f'Загаданные числа это: {firstNum} и {secondNum}.')

''''''
s = int(input('Input Sum: '))
p = int(input('Input Multiplication: '))
for i in range(1,1000):
  for j in range(1,1000):
    if(i + j == s and i*j ==p):
        print(i,j)