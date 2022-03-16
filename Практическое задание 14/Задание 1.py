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
