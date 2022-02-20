# Вариант 7. Создать словарь (Группа – Год_поступления). Написать метод, который удаляет группу с годом поступления 5 и более 5 лет назад.

data = {'Ильин': 2021, 'Савин': 2018, 'Зуев': 2013}
year = 2022

for group in data:
    if year - data[group] <= 5:
        print('Остался:', group)

data = {group: data[group] for group in data if year - data[group] <= 5}
print('Причина:', data)