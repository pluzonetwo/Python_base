# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

def read_file():
    with open("file.txt", "r", encoding="utf-8") as f:
        print('')
        for string in f:
            print(*string.strip().split(";"))
        print('')

def write_file():
    with open("file.txt", "a", encoding="utf-8") as f:
        new_record = input("Введите новую запись: ").replace(" ", ";")
        f.write(f"{new_record}" + "\n")
        print('')

def search_for_entry():
    search_data = input('Введите данные для поиска: ')
    with open('file.txt', 'r', encoding='utf-8') as file:
        find_list = [line.split(';') for line in file if search_data in line]
    if find_list == 0:
        print('Такого контакта нет.')
    print('Найдены следующие контакты: ')
    for i in range(len(find_list)):
        print(f'{i + 1}.', *find_list[i], end = '')
    print('')

def remove_line():
    with open('file.txt', 'r', encoding='utf-8') as file:
        contacts_list = [line for line in file]
        if len(contacts_list) == 0:
            print('Список контактов пуст :(')
            menu()
        else:
            print(*contacts_list)
            remove_data = input('Введите какие контакты вы хотели бы удалить: ')
            with open('file.txt', 'r', encoding='utf-8') as f:
                remove_list = [lines for lines in f if remove_data in lines]
                if remove_list == []:
                    print('Таких данных нет! Попробуйте еще раз.')
                    remove_line()
                else:
                    for i in range(len(remove_list)):
                        contacts_list.remove(remove_list[i])
                    with open('file.txt', 'w', encoding='utf-8') as data:
                            for item in contacts_list:
                                data.write(item)
                                print(end='')
                    read_file()

def change_line():
    search_data = input('Введите имя контакта для изменения: ')
    with open('file.txt', 'r', encoding='utf-8') as file:
        contact_list = [line for line in file]
    with open('file.txt', 'r', encoding='utf-8') as file:
        find_list = [line.split(';') for line in file if search_data in line]
        if find_list == []:
            print('Такого контакта нет.')
        else:
            find_list = input('Введите новые данные: ')
    with open('file.txt', 'r', encoding='utf-8') as file:
        remove_el = [lines for lines in file if search_data in lines]
        for i in range(len(remove_el)):
            contact_list.remove(remove_el[i])
    with open('file.txt', 'w', encoding='utf-8') as data:
        for item in contact_list:
            data.write(item)
    with open('file.txt', 'a', encoding='utf-8') as data:
        data.writelines('\n' + f'{find_list}')

def menu():
    print(
        "1 - посмотр справочника" + "\n" 
        "2 - внести запись в справочник" + "\n"
        "3 - поиск в справочнике" + "\n"
        "4 - изменить запись" + "\n"
        "5 - удалить запись" + "\n"
        "0 - выход"
    )
    task_number = int(input("Введите номер действия: "))
    if task_number == 1:
        read_file()
    elif task_number == 2:
        write_file()
    elif task_number == 3:
        search_for_entry()
    elif task_number == 4:
        change_line()
    elif task_number == 5:
        remove_line()
    else:
        print('До свидания!')
        return    
    menu()

if __name__ == "__main__":
    menu()