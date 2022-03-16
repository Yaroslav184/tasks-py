class Country_1:
    def __init__(self, country='Неизвестно', data='Неизвестно', president='Кто-то', square='Неизвестно'):
        self.country = country
        self.data = data
        self.president = president
        self.square = square

    def __str__(self):
        a = 'Название страны: ' + str(self.country) + ' Дата основания: ' + str(self.data) + ' Президент: ' + str(self.president) + ' Площадь: ' + str(self.square)
        return a

country_1 = Country_1('Россия', '1997', 'Владимир Путин', '17098246')
country_2 = Country_1('Латвия', '1918', 'Эгилс Левитс', '64589')
country_3 = Country_1('Беларусь', '1919', 'Александр Лукашенко', '207600')
print(country_1)
print(country_2)
print(country_3)
print('-------------------------')

class Country_2:
    def __init__(self, country='Неизвестно', data='Неизвестно', president='Кто-то', square='Неизвестно'):
        self.country = country
        self.data = data
        self.president = president
        self.square = square

    def __repr__(self):
        return f'({self.country}, {self.data}, {self.president}, {self.square})'

country_1 = Country_1('Россия', '1997', 'Владимир Путин', '17098246')
country_2 = Country_1('Латвия', '1918', 'Эгилс Левитс', '64589')
country_3 = Country_1('Беларусь', '1919', 'Александр Лукашенко', '207600')
print(country_1)
print(country_2)
print(country_3)
print('-------------------------')
b = [country_1, country_2, country_3]
print(b)
print(type(b))
