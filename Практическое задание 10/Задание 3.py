# Вариант 7

import random as rand

matrix = []

Rows = 8
Columns = 8

MIN_GENERATED_NUMBER = -5
MAX_GENERATED_NUMBER = 20

for Row in range(Rows):
    matrix.append([])
    for Column in range(Columns):
        # Заполняем случайными числами от MIN_GENERATED_NUMBER до MAX_GENERATED_NUMBER
        matrix[Row].append(rand.randint(MIN_GENERATED_NUMBER, MAX_GENERATED_NUMBER))

# Вывод матрицы
print('Созданная матрица 8х8:')
for Row in range(len(matrix)):
    for Column in range(len(matrix[Row])):
        print(matrix[Row][Column], end=' ')
    print()
print()

# Поиск "таких k, что элементы k-й строки матрицы совпадают с элементами k-ого столбца."
for Column in range(Columns):
    column_elements = []
    matching_elements = []
    for Row in range(Rows):
        column_elements.append( matrix[Row][Column] )

    for Element in column_elements:
        if Element in matrix[Column]:
            matching_elements.append(Element)

    print('Совпадающие элементы K-Строки и K-Столбца: {}'.format(matching_elements))
print()

for Row in range(Rows):
    # Обозначаем нужду вывода строки как найденной
    need_print = False
    # Общая сумма элементов строки
    row_summary = 0
    for Column in range(Columns):
        # Суммируем элементы строки
        row_summary = row_summary + matrix[Row][Column]
        # Проверяем, есть ли элемент меньше 0
        if matrix[Row][Column] < 0:
            # Разрешаем вывод строки как определённой по условию
            need_print = True
    if need_print:
        print('Строка №{} имеет отрицательный элемент. Сумма элементов строки: {}'.format(Row+1, row_summary))