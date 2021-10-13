""" Задание №5: В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве."""

import random

rand_int = [random.randint(-205, 205) for _ in range(30)]
print('Наш массив представлен числами: ', rand_int)

our_index = 0

for x in rand_int:
    if rand_int[our_index] > x:
        our_index = rand_int.index(x)

if rand_int[our_index] >= 0:
    print('В массиве ни имеетеся элементов с отрицательным знаком!!!')
else:
    print('В массиве минимальным отрицательным элементов является', rand_int[our_index], 'и находится'
         ' на позиции', our_index)


