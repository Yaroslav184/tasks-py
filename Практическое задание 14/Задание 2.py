# Задание №2
# Ильин Ярослав 1993
# Вариант 9

import math

def z1(chislo):
   z1 = 4 * math.sin(chislo / 2) * math.cos(5 * chislo / 2)
   return z1

def z2(chislo):
   z2 = 2 * math.sin(chislo)
   return z2

chislo = int(input('Введите число: '))

z1_and_z2 = str(z1(chislo)) + ', ' + str(z2(chislo))

with open('file.txt', 'w') as result:
    result.write(z1_and_z2)
    print('Файл создан! Смотрите результат.')

result.close()