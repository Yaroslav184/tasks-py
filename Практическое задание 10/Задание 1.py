# Вариант 7

import random as rand

# Создаём переменные для мин. и макс. числа
matrix_min = matrix_max = None

# DEBUG - режим для автозаполнения чисел
debug = False

matrix = []

Rows = 3
Columns = 3

for Row in range(Rows):
    matrix.append([])
    for Column in range(Columns):
        if debug:
            # Случайное число от 0 до 50, для большего разброса минимального и максимального числа
            number = rand.randint(0, 50)
            # Запись в матрицу
            matrix[Row].append(number)
            # Вывод информации DEBUG действия
            print('[ DEBUG ] Сгенерировал число \"{}\" для позиции матрицы: matrix[{}][{}].'.format(number, Row, Column))
        # Если выключен режим DEBUG
        else:
            while True:
                try:
                    number = int(input('Введите число для записи в ячейку матрицы [{}][{}]: '.format(Row, Column)))
                    break
                except ValueError:
                    print('Введите число!')
            matrix[Row].append(number)

        # Запись в минимальное или максимальное число
        # Проверка на минимальное
        if matrix_min is None or number < matrix_min:
            # Записываем как минимальное число
            matrix_min = number
        # Проверка на максимальное
        if matrix_max is None or number > matrix_max:
            # Записываем как максимальное число
            matrix_max = number

print('Структура матрицы:')
for Row in range(Rows):
    for Column in range(Columns):
        print(matrix[Row][Column], end=" ")
    print()
print()

print('Минимальное число в матрице: {}'.format(matrix_min))
print('Максимальное число в матрице: {}'.format(matrix_max))