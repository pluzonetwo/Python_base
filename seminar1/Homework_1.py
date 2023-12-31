# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Решение:
# inputNum = int(input('Введите трехзначное число: '))
# num1 = int(inputNum / 100)
# num2 = int(inputNum % 100 / 10)
# num3 = inputNum % 10
# result = num1 + num2 + num3
# print(f'{num1}, {num2}, {num3}')
# print('Сумма цифр введенного числа: 'f'{result}')
# Вариант 2
# summa = 0
# while n > 0:
#     ost = n % 10
#     n = n // 10
#     summa += ost

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# Решение:
# sumOfBirds = int(input('Введите общее количество журавликов: '))
# birdsOfPetya = int(sumOfBirds / 3 / 2)
# birdsOfSergey = int(birdsOfPetya)
# birdsOfKatya = int(sumOfBirds / 3 * 2)
# print("Катя сделала: "f'{birdsOfKatya} ''журавликов, а Петя и Сережа сделали по' f' {birdsOfPetya}' '!')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# Решение:
# inputNum = input('Введите шестизначное число: ')

# isFiveDigit = len(inputNum) != 5

# if isFiveDigit:
#     print('Необходимо ввести шестизначное число!')
# else:
#     num1 = int(inputNum[0])
#     num2 = int(inputNum[1])
#     num3 = int(inputNum[2])
#     num4 = int(inputNum[3])
#     num5 = int(inputNum[4])
#     num6 = int(inputNum[5])

#     result1 = num1 + num2 + num3
#     result2 = num4 + num5 + num6

#     if result1 == result2:
#         print('Yes!')
#     else:
#         print('No!')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

# Решение:
# lengthOfChocolate = int(input('Введите длину шоколадки: '))
# widthOfChocolate = int(input('Введите ширину шоколадки: '))
# numOfSlices = int(input('Сколько долек вы хотите отломить: '))
# areaOfChocolate = lengthOfChocolate * widthOfChocolate
# if areaOfChocolate % numOfSlices == 0 or numOfSlices % areaOfChocolate == 0:
#     print('Yes!')
# else:
#     print('No!')
