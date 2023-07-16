# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

def read_file():
    with open("file.txt", "r", encoding="utf-8") as f:
        for string in f:
            print(*string.strip().split(";"))

def write_file():
    with open("file.txt", "a", encoding="utf-8") as f:
        new_record = input("Введите новую запись ").replace(" ", ";")
        f.write(f"{new_record}" + "\n")

def search_for_entry():
    search_data = input('Введите данные для поиска: ').replace(" ", ";")
    with open('file.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    print(data)        

def menu():
    print(
        "1 - посмотр справочника" + "\n" 
        "2 - внести запись в справочник" + "\n" + 
        "3 - поиск в справочнике" + "\n"
        "4 - выход"
    )
    task_number = int(input("Ввведите номер действия: "))
    if task_number == 1:
        read_file()
    elif task_number == 2:
        write_file()
    elif task_number == 3:
        search_for_entry()
    else:
        print('До свидания!')
        return
    menu()

if __name__ == "__main__":
    menu()