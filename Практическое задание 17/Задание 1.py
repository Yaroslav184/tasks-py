class Educational:
    def __init__(self, educational='Неизвестно', city='Неизвестно'):
        self.educational = educational
        self.city = city

    def __str__(self):
        a = 'Название учебного заведения: ' + str(self.educational) + ' | Город: ' + str(self.city)
        return a

educational_1 = Educational('ССУЗ', 'Москва')
educational_2 = Educational('ВУЗ', 'Великий Новгород')
print('1)', educational_1)
print('2)', educational_2)
