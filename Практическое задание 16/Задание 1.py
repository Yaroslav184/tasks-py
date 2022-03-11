# Задание №1
# Ильин Ярослав 1993
# Вариант 9

class Country:
    def __init__(self, country='Неизвестно', data=1, president='Кто-то', square=1):
        self.country = country
        self.data = data
        self.president = president
        self.square = square
        print('Создан!')
        print('-----------------------')

self1 = Country('Россия', 1997, 'Владимир Путин', 17098246)

def countryInfo():
    print('Название страны:', self1.country)
    print('Дата основания:', self1.data)
    print('Президент:', self1.president)
    print('Площадь:', self1.square)

countryInfo()