# Задание №1
# Ильин Ярослав 1993
# Вариант 6

file_name = input('Введите название файла: ')
file = open(file_name, 'w')

print('Содержимое файла:')

while True:
    s = input()
    if s == '':
        break
    file.write(s + '\n')
print('Файл создан!')
file.close()