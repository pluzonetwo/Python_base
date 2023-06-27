import time
# from time import time # импорт только функцию time
from sys import getsizeof

# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# string = 'a a a b c a a d c d d'.replace(' ', '')
# answer = ''
# for elem in string:
#     print(elem)

# string = 'a a a b c a a d c d d'.split()
# # print(*string, sep='\n')
# # print(*string, end=', ')
# answer = ''
# new_list = []
# for elem in string:
#     if elem in new_list:
#         answer += elem + '_' + str(new_list.count(elem)) + ' '
#     else:
#         answer += elem + ' '
#     new_list.append(elem)
# print(answer)

# Более оптимальный вариант через словарь
# start = time.time()
# string = ('a a a b c a a d c d d'*10).split()
# answer = ''
# my_dict = {}
# for elem in string:
#     if elem in my_dict:
#         answer += elem + '_' + str(my_dict[elem]) + ' '
#         my_dict[elem] += 1
#     else:
#         answer += elem + ' '
#         my_dict[elem] = 1
# print(answer)
# finish = time.time()
# print(finish - start)
# print(getsizeof(my_dict))
# print(getsizeof(answer))

# Множество
# my_set = set() # создает пустое множество
# my_set = {1, 5 , 3, 7} # создаем заполненное множество
# все повторяющиеся значения в множестве игнорируются
# my_list = [1, 2, 3, 4, 1, 2, 3, 5, 7, 8, 8]
# my_set = set(my_list)
# print(len(my_set))
# my_set.add() # добавить
# my_set.remove() # удалить
# другие функции в лекции

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

string = input('Input text: ').lower()
my_list = string.split(' ')
answer = 0
new_list = []
my_dict = {}
max = 0

for el in my_list:
    if el in my_dict:
        my_dict[el] += 1
    elif el not in my_dict:
        answer += 1
        my_dict[el] = 1
    if my_dict[el] > max:
        max = my_dict[el]

for el in my_dict:
    if my_dict[el] == max:
        print('{} встречается {} раз'.format(el, my_dict[el]))

print(my_dict)
print(answer)

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

