def sets():
    x1 = {6, 7, 4, 9}
    x2 = {0, 2, 3, 7, 8, 9, 10}
    x3 = x1.difference(x2)
    print('Элементы множества x1:', x1)
    print('Элементы множества x2:', x2)
    print('Элементы множества x3:', x3)
    x = int(input('Введите число: '))
    if x in x3:
        x3.remove(x)
    print('Элементы множества x3:', x3)

sets()
