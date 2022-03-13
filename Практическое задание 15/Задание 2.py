import os.path

file_name = 'file'

try:
    with open(file_name, encoding='utf-8') as file:
        contents = file.read()
        
except FileNotFoundError:
    print(f'Запрашиваемый файл {file_name} не найден!')

else:
    print(f'Запрашиваемый файл {file_name} найден!')

# Если текстовый файл существует
if os.path.exists('file'):
    a = open('file', 'r')
    print('Файл существует!')
    print('Содержимое файла:', *a)

# Если файл НЕ существует, то создадим новый текстовый файл
else:
    new_file = open('file', 'w')
    # Запись текста в этот файл
    new_file.write('Hello World! My name is Yaroslav.')
    print('Файл не существует. Мы создали новый, перезапустите программу!')
