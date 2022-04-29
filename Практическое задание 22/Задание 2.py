import re

def main():
    print('Введите строку: ')
    string = input()
    print('Нажмите ENTER!')
    number = input()
    print(replace_number(string, number))

def replace_number(string, number):
    return re.sub(r'\d+', lambda m: str(int(m.group()) ** 3), string)

main()