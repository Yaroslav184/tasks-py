# Вариант 9. Подсчитать количество букв латинского алфавита в данной строке.

# Обозначаем алфавит, по которому будем проверять
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Переменная для подсчёта кол-ва букв
letters_count = 0

# Просим пользователя ввести текст
text = input("[ * ] Введите текст: ")

# Считаем латинские буквы
for letter in text.lower():
    # Если буква находится в алфавите
    if letter in alphabet:
        # Увеличиваем счётчик букв
        letters_count = letters_count + 1

# Выводим результат
print('Ведённый текст: {}'.format(text))
print('Кол-во букв латинского алфавита: {}'.format(letters_count))