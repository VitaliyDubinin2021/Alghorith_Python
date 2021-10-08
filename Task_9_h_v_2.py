""" Задание №9: Среди натуральных чисел, которые были введены, найти наибольшее по
сумме цифр. Вывести на экран это число и сумму его цифр. """

def numbers_summ(numb):
    summ_number = 0
    for i in numb:
        summ_number += int(i)
    return summ_number

our_list = [x for x in input('Здравствуйте! Введите последовательность чисел через пробел: ').split()]

maximal_our_number = 0
maximal_our_summ = 0
for x in our_list:
    if numbers_summ(x) > maximal_our_summ:
        maximal_our_number = x
        maximal_our_summ = numbers_summ(x)

print(f'Число {maximal_our_number} имеет наибольшую сумму цифр {maximal_our_summ}')






