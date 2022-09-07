# Реализуйте алгоритм перемешивания списка.

import random
list_input = list(range(-10, 10, 3))
print(f'    Исходный список: {list_input}')
random.shuffle(list_input)
print(f'Перемешанный список: {list_input}')