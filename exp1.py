# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Введите число: '))
string = str(number)
sum = 0
for i in string:
    if(i != '.'):
        sum += int(i)
print(sum)