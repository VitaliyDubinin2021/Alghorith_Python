""" Задание №3: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

rand_int = [random.randint(0, 999) for _ in range(20)]
maximal = rand_int[0]
minimal = rand_int[0]
print('Массив до внесения правок: ', rand_int)

for x in rand_int:
    if x > maximal:
        maximal = x
    elif x < minimal:
        minimal = x

maximal_index = rand_int.index(maximal)
minimal_index = rand_int.index(minimal)
rand_int[minimal_index], rand_int[maximal_index] = rand_int[maximal_index], rand_int[minimal_index]

print(f'Наш массив после внесения изменений: {rand_int}, местами поменяли индексы максимальный {maximal_index} '
      f'и минимальный {minimal_index}')
