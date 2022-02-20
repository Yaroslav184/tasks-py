# Вариант 7

import random as rand

def PrintMatrix(matrix):
    for Row in range(len(matrix)):
        for Column in range(len(matrix[Row])):
            print(matrix[Row][Column], end=" ")
        print()
    print()

matrix = []

Rows = 5
Columns = 5

for Row in range(Rows):
    # Добавляем массив
    matrix.append([])
    for Column in range(Columns):
        # Добавляем случайное число от -30 до 30
        matrix[Row].append(rand.randint(-30, 30))

# Выводим изначальную матрицу
print('Изначальная структура матрицы:')
PrintMatrix(matrix)

# Изменяем все отрицательные значения на положительные
for Row in range(Rows):
    for Column in range(Columns):
        if matrix[Row][Column] < 0:
            matrix[Row][Column] = matrix[Row][Column] * -1

# Выводим изменённую матрицу
print('Изменённая структура матрицы:')
PrintMatrix(matrix)