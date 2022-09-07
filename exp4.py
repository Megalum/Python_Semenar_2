# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
number = int(input('Введите число: '))
list = []
for i in range(number):
    list.append(random.randint(-number, number))
print(f'Исходые значения списка: {list}')

file = open('file.txt', 'r') #6, 4, 2, 1, 0
output = 1
for i in file.read():
    if (i != '\n'):
        output *= list[int(i)]
print(f'Произведение чисел: {output}')