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

# output = is_rythm(generated_string(phrase), is_count_lowels(generated_string(phrase), vowels), vowels)

# def res(data):
#     if data:
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')

# res(output)