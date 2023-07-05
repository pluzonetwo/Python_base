# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# first_elem = int(input('Введите первый элемент арифметической прогрессии: '))
# step = int(input('Введите шаг арифметической прогрессии: '))
# quantity_elem = int(input('Введите количество элементов арифметической прогрессии: '))

# array = []

# def fill_array(arr, el):
#     for i in range(1, quantity_elem + 1):
#         arr.append(el)
#         el += step
#     return arr

# print(fill_array(array, first_elem))


# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).

# minimum = int(input('Input min num: '))
# maximum = int(input('Input max num: '))

# array = [-1, -2, -3, 1, 2, 3, 4, 5, -10, -15, -5]

# def find_range(arr, less, greater):
#     return [i for i in arr[0:] if i >= less and i <= greater]

# print(find_range(array, minimum, maximum))