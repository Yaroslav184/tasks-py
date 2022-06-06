n = int(input('Введите число: '))

def fibonacci(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print('Определенное число:', fibonacci(n))