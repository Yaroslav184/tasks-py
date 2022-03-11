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

def __init__(self, country='Неизвестно', data=1, president='Кто-то', square=1):
    self.country = country
    self.data = data
    self.president = president
    self.square = square

self2 = Country('Латвия', 1918, 'Эгилс Левитс', 64589)

def countryInfo():
    print('Название страны:', self2.country)
    print('Дата основания:', self2.data)
    print('Президент:', self2.president)
    print('Площадь:', self2.square)

countryInfo()

def __init__(self, country='Неизвестно', data=1, president='Кто-то', square=1):
    self.country = country
    self.data = data
    self.president = president
    self.square = square

self3 = Country('Беларусь', 1919, 'Александр Лукашенко', 207600)

def countryInfo():
    print('Название страны:', self3.country)
    print('Дата основания:', self3.data)
    print('Президент:', self3.president)
    print('Площадь:', self3.square)

countryInfo()
