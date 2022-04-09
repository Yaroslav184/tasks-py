import random

def spisok():
    a = [random.randint(0, 9) for i in range(10)]
    print('Список чисел:', a)
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print('Различные числа из списка:', b)
    print('Длинна различных чисел из списка:', len(b))

spisok()
