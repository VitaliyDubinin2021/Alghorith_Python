""" Задание №6: В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать."""

import random

rand_int = [random.randint(0, 99) for _ in range(10)]
print('Наш массив представлен числами', rand_int)

summ = 0  #Сумма чисел между минимальным и максимальным элементами

index_minimal = 0
index_maximal = 0

step_index = 1

for x in rand_int:
    if rand_int[index_minimal] > x:
        index_minimal = rand_int.index(x)
    elif rand_int[index_maximal] < x:
        index_maximal = rand_int.index(x)

if index_maximal - index_minimal < 0:
    step_index = -1

for x in rand_int[index_minimal + step_index:index_maximal:step_index]:
    summ += x

print('Сумма элементов между минимальным и максимальным', rand_int[index_minimal], 'и', rand_int[index_maximal],
      'cоответственно элементами равна', summ)


