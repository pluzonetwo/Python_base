# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам

# vowels = {1: 'а', 2: 'я', 3: 'у', 4: 'ю', 5: 'о', 6: 'е', 7: 'ё', 8: 'э', 9: 'и', 10: 'ы'}
# phrase = input('Input line of poem: ')

# generated_string = lambda phrase: phrase.split()

# def is_count_lowels(lines, dictionary):
#     result = 0
#     for i in lines[0]:
#         for key, value in dictionary.items():
#             if i == value:
#                 result += 1
#     return result

# def is_rythm(lines, count, dictionary):
#     for i in range(1, len(lines)):
#         last_count = 0
#         for i in lines[i]:
#             for key, value in dictionary.items():
#                 if i == value:
#                     last_count += 1
#         if last_count != count:
#             return False
#     return True

# def res(data):
#     if data:
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')

# output = is_rythm(generated_string(phrase), is_count_lowels(generated_string(phrase), vowels), vowels)

# res(output)

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны 
# быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая 
# операция, у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# def print_operation_table(func, num_rows = 6, num_cols = 6):
#   for i in range(1, num_rows):
#     string = ' '
#     for j in range(1, num_cols):
#       string = string + str(func(i, j)) + ' '
#     print(string + '\t')

# print_operation_table(lambda x, y: x * y)

