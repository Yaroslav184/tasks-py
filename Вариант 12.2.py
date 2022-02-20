# Вариант 12
import math
import random

a = random.random() # float(input("Введите сторону a: "))
b = random.random() # float(input("Введите сторону b: "))
if a > 10 or b > 10:
    print("Длины сторон катетов прямоугольного треугольника не могут быть больше 10 см.")
s = a * b / 2
print("Площадь прямоугольного треугольника равна:", round(s, 2))
c = math.sqrt(a**2 + b**2)
p = a + b + c
print("Периметр прямоугольного треугольника равен:", round(p, 2))