# def calc_sum(a):
#     return a + a

# def calc_multi(a):
#     return a * a

# def math(func, arg):
#     print(func(arg))

# math(calc_sum, 5)

# def calc_sum(a, b):
#     return a + b
# or
# calc_sum = lambda a, b: a + b

# def calc_multi(a, b):
#     return a * b

# def math(func, arg1, arg2):
#     print(func(arg1, arg2))

# # math(calc_sum, 5, 45)
# math(lambda a, b: a + b, 5, 45)

# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# Var1
# array = [1, 2, 3, 4, 56, 76, 456, 9]

# def func(arr):
#     new_tuple = list()
#     for i in arr:
#         if i % 2 == 0:
#             new_tuple.append((i, i ** 2))
#     return new_tuple

# print(func(array))

# # Var2
# array = [1, 2, 3, 4, 56, 76, 456, 9]

# def select(func, arr):
#     return [func(x) for x in arr]

# def where(func, new_arr):
#     return [x for x in new_arr if func(x)]

# new_array = select(int, array)
# new_array = where(lambda x: x % 2 == 0, new_array)
# new_array = list(select(lambda x: (x, x ** 2), new_array))
# print(new_array)

# Var 3
# array = [1, 2, 3, 4, 56, 76, 456, 9]

# new_array = map(int, array)
# new_array = filter(lambda x: x % 2 == 0, new_array)
# new_array = list(map(lambda x: (x, x ** 2), new_array))
# print(new_array)

# Method Map
# array = [x for x in range(1, 10)]
# print(array)
# new_array = list(map(lambda x: x + 10, array))
# print(new_array)

# # Method Filter
# data = [5, 46, 55, 34, 105, 125, 68]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# # Method zip
# test_zip = list(zip(
#     [1, 2, 3],
#     ['a', 'b', 'c'],
#     ['а', 'б', 'в']
# ))
# print(test_zip)
# метод zip пробегает по минимальному входящему набору

# # Method enumerate
# # Позволяет пронумеровать набор данных
# users = ['user_1', 'user_2', 'user_3']
# data = list(enumerate(users))
# print(data)

# Работа с файлами
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a', encoding='utf-8')
# data.writelines(colors)
# data.close

# with open('file.txt', 'w') as data:
#     data.write('line_1\n')
#     data.write('line_2\n')

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

