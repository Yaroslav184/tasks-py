import re

N = 2
strings = []

for i in range(0, N):
    print('Введите строку:', end=' ')
    strings.append(input())

print('Введите слог:', end=' ')
a = input()

for string in strings:
    count = len(re.findall(a, string))
    print('Слог \'%s\' встречается в 1-ой строке %s раз' % (a, count))
    print('Слог \'%s\' встречается во 2-ой строке %s раз' % (a, count))
