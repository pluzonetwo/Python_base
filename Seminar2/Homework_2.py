# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2

# Решение:
# вариант 1
# result = 0

# for i in 0, 1, 0, 1, 0, 1:
#     print(i)
#     if i == 0:
#         result += 1

# print(result)

# # Вариант 2
# import random
# quantity_coins = int(input('Input quantity of coins: '))
# iter = 0
# result = 0
# while iter < quantity_coins:
#     for i in 0, 1:
#         print(i)
#     # random_numbers = random.randint(0, 1)
#     # print(random_numbers)
#     iter += 1

# Вариант (эталон)
# n = int(input('Inpit quantity of coins: '))
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = input('орел или решка? ')
#     if x == 'орел':
#         count_zero += 1
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# sum_x_and_y = int(input('Input sum x and y: '))
# mul_x_and_y = int(input('Input multipilicate x and y: '))

# for i in range(1000):
#     for j in range(1000):
#         if sum_x_and_y == i + j and mul_x_and_y == i * j:
#             print("Numbers is " f'{i}' " and " f'{j}')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# maxNum = int(input('Input max num: '))

# Вариант 1
# for i in range(maxNum):
#     if 2 ** i < maxNum:
#         print(2 ** i)

# Вариант 2
# maxNum = int(input('Input max num: '))
# i = 0

# while 2 ** i <= maxNum:
#     print(2 ** i)
#     i += 1