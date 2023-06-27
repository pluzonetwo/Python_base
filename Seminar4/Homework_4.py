# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

size_multy_1 = int(input('Input a quantity of mul 1: '))
size_multy_2 = int(input('Input a quantity of mul 2: '))

multy_1 = set()
multy_2 = set()

for elem_1 in range(size_multy_1):
    input_data_1 = int(input('Input number 1: '))
    multy_1.add(input_data_1)

for elem_2 in range(size_multy_2):
    input_data_2 = int(input('Input number 2: '))
    multy_2.add(input_data_2)

print(multy_1)
print(multy_2)

same_elem = multy_1.intersection(multy_2)

same_elem_list = list(same_elem)
min = same_elem_list[0]

print(sorted(same_elem_list))