import re

def stroka():
    string = input('Введите строку: ')
    pattern = r'\*q\+'
    if re.search(pattern, string):
        print('В строке есть подстрока *q+')
    else:
        print('В строке нет подстроки *q+')

stroka()