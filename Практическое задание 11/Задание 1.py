# Вариант 7

import random

n = int(input('Введите число для n: '))

def Tuple(count, min, max):
    tmp_tuple = tuple()
    for i in range(count):
        tmp_tuple = tmp_tuple + (random.randint(min, max), )
    return tmp_tuple

tuple_1 = Tuple(10, 0, n)

tuple_2 = Tuple(10, -n, 0)

tuple_3 = tuple_1 + tuple_2

print(f'Кортеж 3: {tuple_3}')
print(f'Кол-во нулей в 3 кортеже: {tuple_3.count(0)}')