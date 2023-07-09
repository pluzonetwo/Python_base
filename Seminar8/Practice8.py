# f = open('my_file.txt', 'r') # если не указывать 2-ой аргумент, то режим чтения будет по умолчанию.
# f.read()
# f.close()

# with open('file.txt', 'r') as f:
#     st = f.read()
# print(st)

# # Считает только 1 строку
# with open('file.txt', 'r') as f:
#     st = f.readline()
# print(st)

# # Считает и сохранит в список
# with open('file.txt', 'r') as f:
#     st = f.readlines()
# print(st)

# with open('file.txt', 'r') as f:
#     for string in f:
#         print(string)

# with open('file.txt', 'r') as f:
#     for string in f:
#         a = int(string)
#         print(a)

# with open('file.txt', 'r') as f:
#     my_list = [int(i) for i in f]
# print(my_list)

# array = [1, 2, 4, 5]
# array = list(map(lambda x: str(x) + '\n', array))
# with open('file.txt', 'w') as f:
#     f.writelines(array)

# Modul OS
# import os

# os.chdir('new_dir') # переместит в эту папку
# print(os.getcwd()) # покажет текущую рабочую директорию

# Modul Shatil

# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def print_info(temp):
    print(temp)

def read_file():
    with open('file.txt', 'r', encoding='utf-8') as f:
        for string in f:
            print(string)

def write_file():
    with open('file.txt', 'a') as f:
        name = input('Input a name: ')
        surname = input('Input a surname: ')
        p_surname = input('Input a p_surname: ')
        phone = input('Input a phone number: ')
        entry = '\n' + name + ';' + surname + ';' + p_surname + ';' + phone
        f.writelines(entry)

def search_for_entry():
    pass

def menu():
    data = read_file()
    flag = True
    while flag:
        n = int(input('1 - поиск из справочника, 2 - запись в справочник, 3 - поиск, 0 - выход\n'))
        if n == 1:
            read_file()
        elif n == 2:
            write_file()
        elif n == 3:
            search_for_entry() 
        elif n == 0:
            flag = False   
        else:
            print('Введите корректное значение')

if __name__ == '__main__':
    menu()

import os
from random import randint

# Var 2
# def read_file():
#     with open("phonebook.txt", "r", encoding="utf - 8") as f:
#         for string in f:
#             print(*string.strip().split(";"))


# def write_file():
#     with open("phonebook.txt", "a", encoding="utf - 8") as f:
#         new_phone = input("Введите новую запись ").replace(" ", ";") + "\n"
#         f.write(new_phone)


# def menu():
#     print(
#         "Нажмите 1 если хотите посмотреть справочник, Нажмите 2 если хотете внести запись или 3 что бы выйти из меню"
#     )
#     task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))
#     if task_number == 1:
#         read_file()
#     elif task_number == 2:
#         write_file()

#     menu()


# if __name__ == "__main__":
#     menu()



