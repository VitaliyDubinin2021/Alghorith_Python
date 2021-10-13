""" Задание №4: Определить, какое число в массиве встречается чаще всего."""

import random

rand_int = [random.randint(0, 10) for _ in range(10)]
print('Наш сформированный из случайных чисел массив', rand_int)

our_index = 0
for x in rand_int:
    if rand_int.count(our_index) < rand_int.count(x):
        our_index = rand_int.index(x)

print('Число', rand_int[our_index], 'встречается', rand_int.count(our_index), 'раз/раза')

