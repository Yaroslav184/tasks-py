import sys

def main():
    if len(sys.argv) != 2:
        print('Использование: {} <число>'.format(sys.argv[0]))
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 1:
        print('Число должно быть неотрицательным')
        sys.exit(1)

    a = [int(x) for x in input('Введите последовательность чисел через пробел: ').split()]
    if len(a) != n:
        print('Число элементов в последовательности должно совпадать с заданным')
        sys.exit(1)

    p = [a[0]]
    for i in range(1, n):
        p.append(a[i] * p[i - 1])

    print('Последовательность частичных произведений:')
    for i in range(n):
        print('P{} = {}'.format(i + 1, p[i]))

main()