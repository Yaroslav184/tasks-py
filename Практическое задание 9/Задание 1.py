import random

# Список номеров
numbers = []
# Общая сумма чисел списка
total = 0

# Создаём 50 чисел
for i in range(50):
    # Создаём число от 0 до 20
    number = random.randint(0, 20)
    # Добавляем в список
    numbers.append(number)
    # Суммируем общую сумму чисел
    total = total + number

# Выводим результаты
print('Список номеров: {}'.format(numbers))
print('Среднее арифметическое списка: {}'.format(total/len(numbers)))
