import random

# Массив, где будут цифры
arr = []

# Заполнение 20 случайными целыми числами
for i in range(20):
    # Генерация числа от 0 до 20
    number = random.randint(0, 20)
    # Добавление числа в массив
    arr.append(number)

# Проверка массива, вывод на экран
print('Случайно сгенерированный массив: {}'.format(arr))

# Распределение цифр
even_numbers = []  # Чётные числа
odd_numbers = []  # Нечётные числа

# Перебираем все цифры, что создали ранее
for number in arr:
    # Проверяем на чётность по остатку деления на 2
    if number % 2 == 0:
        # Если чётное - добавляем в массив чётных
        even_numbers.append(number)
    else:
        # Если нечётное - добавляем в массив нечётных
        odd_numbers.append(number)

# Вывод распределённых массивов
print('Чётные числа: {}'.format(sorted(even_numbers)))
print('Нечётные числа: {}'.format(sorted(odd_numbers)))

# Соединяем чётные и нечётные
arr = sorted(even_numbers) + sorted(odd_numbers)

# Вывод результата
print('Итоговое значение фильтрации массива: {}'.format(arr))
