""" Задание №1: В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

our_result = {}
for n in range(2, 10):
    our_result[n] = []
    for f in range(2, 100):
        if f % n == 0:
            our_result[n].append(f)
    print(f'Для конкретного числа {n} кратны - {len(our_result[n])}. Список кратных чисел: {our_result[n]}.')



