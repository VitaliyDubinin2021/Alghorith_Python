""" Задание №1:  Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль
выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего. """

import collections

storage = collections.namedtuple('storage', ['n1', 'n2', 'n3', 'n4'])

p = int(input("Здравствуйте! Введите требуемое количество предприятий: "))
base_storage = {}

for i in range(p):
    name = input('Рассматриваем ' + str(i+1) + ' -ое предприятие: ')
    profit_n1 = int(input('Прибыль предприятия за 1-й квартал года: '))
    profit_n2 = int(input('Прибыль предприятия за 2-й квартал года: '))
    profit_n3 = int(input('Прибыль предприятия за 3-й квартал года: '))
    profit_n4 = int(input('Прибыль предприятия за 4-й квартал года: '))
    base_storage[name] = storage(n1 = profit_n1,
                                 n2 = profit_n2,
                                 n3 = profit_n3,
                                 n4 = profit_n4)

import random

base_storage['Производитель №1'] = storage(n1 = random.randint(25, 2500),
                                           n2 = random.randint(5, 1475),
                                           n3 = random.randint(120, 2401),
                                           n4 = random.randint(106, 515))

base_storage['Производитель №2'] = storage(n1=random.randint(200, 4501),
                                           n2=random.randint(200, 4300),
                                           n3=random.randint(300, 500),
                                           n4=random.randint(20, 700))

our_prof = ()

for name, prof in base_storage.items():
    our_prof += prof

avg_prof = sum(our_prof) / len(base_storage)
print(f'Средняя прибыль за год для всех предприятий {round(avg_prof, 1)}')

for name, prof in base_storage.items():
    if sum(prof) > avg_prof:
        print(f'Выше среднего {name} - {sum(prof)}')
    else:
        print(f'Ниже среднего {name} - {sum(prof)}')


