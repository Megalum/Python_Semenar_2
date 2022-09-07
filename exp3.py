# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def func(n):
    return (1 + (1 / n)) ** n

number = int(input('Введите число: '))
list = {}
sum = 0
for i in range(1, number + 1):
    list[i] = func(i)
    sum += list[i]
print(round(sum.real, 3))