# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# def exp(a, b):
#     if b == 1:
#         return a
#     else:
#         return exp(a, b - 1) * a

# print(exp(3, 5))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

# def summa(a, b):
#     if a == b:
#         return a + b
#     elif a > b:
#         return summa(a - 1, b) + 1
#     elif a < b:
#         return summa(a + 1, b) - 1
    
# print(summa(6, 4))