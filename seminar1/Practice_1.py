# a = int(input('Input a: '))
# b = int(input('Input b: '))

# c = a + b

# print(c)

# a = int(input('Input your age: '))

# if a >= 18:
#     print('OK!')
# else:
#     print('NOT OK')

# Задача № 1
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# s = v × t.

# Решение:
# n = int(input('Введите количество километров в день: '))
# m = int(input('Длина маршрута: '))

# res = int(bool(m % n))
# days = m //n + res

# print (n, m, days)

# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# class1 = 20
# class2 = 21
# class3 = 22

# sum_class = (class1 + class2 + class3) / 2 + 0.5

# print(int(sum_class))

# desksOfClass1 = int(class1 / 2 + 0.5)
# desksOfClass2 = int(class2 / 2 + 0.5)
# desksOfClass3 = int(class3 / 2 + 0.5)

# print(f'{desksOfClass1} {desksOfClass2} {desksOfClass3}')

# firstClass = int(input('Enter A: '))
# secondClass = int(input('Enter B: '))
# thirdClass = int(input('Enter C: '))

# desksAmount = ((firstClass // 2) + (firstClass % 2))+ ((secondClass // 2) + (secondClass % 2)) + ((thirdClass // 2) + (thirdClass % 2))
# print(desksAmount)

# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# var1 = int(input('Введите номер вагона i: '))
# var2 = int(input('Введите номер вагона j: '))

# print(f'Общая длина состава {var1 + var2 - 1}')

# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

year = int(input('Введите год: '))
var1 = year % 100
var2 = year % 4
var3 = year % 400

if (var2 == 0 and var1 != 0) or var3 == 0:
    print('YES')
else:
    print('NO')

# if var2 == 0 and var3 != 0 and var1 != 0:
#     print('YES')
# else:
#     print('NO')
