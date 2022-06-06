import math

def main(x):
    x = math.cosh(float(input('Введите число: ')))
    print(x)
    return 1 + x * x * factorial(2)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# x = math.cosh(float(input('Введите число: ')))
#
# print(x)
print(main(x=float(input('Введите число: '))))