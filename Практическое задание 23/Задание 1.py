def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n = int(input('Введите число 3 или 4: '))
    for i in range(n + 1):
        print(factorial(i), end=' ')
    print()
    for i in range(n + 1):
        print(i, factorial(i), end=' ')
    print()

main()