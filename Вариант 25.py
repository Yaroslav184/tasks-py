# 25 вариант
# import math
# a = float(input('Введите сторону a = '))
# b = float(input('Введите сторону b = '))
# c = float(input('Введите сторону c = '))
# p = (a + b + c) / 2
# s = float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
# print('Площадь треугольника:', s)

from figurs import rectangle
a = float(input('Введите сторону a = '))
b = float(input('Введите сторону b = '))
c = float(input('Введите сторону c = '))
print('Площадь треугольника:'%rectangle(a, b, c))