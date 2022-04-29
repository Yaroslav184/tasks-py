import re

def stroka():
    string = 'Сколько будет 2+3?'
    pattern = r'2\+3'
    result = re.findall(pattern, string)
    print(result)

stroka()