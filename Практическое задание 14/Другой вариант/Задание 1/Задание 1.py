"""
В файле date.txt, содержаться различные даты.
Для каждой даты указать число, месяц и год, номер дня в году.
Для этого файла предусмотреть ввод данных в файл и вывод на экран

Содержание файла:
31.07.2021
23.11.1992
03.05.2013
04.08.2011
19.01.2014
06.01.2014
19.07.1961
"""

def get_date(date):
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:])
    day_in_year = (day + (31 * (month - 1)) + ((year - 1) * 365) + ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)) % 7
    return day_in_year

def main():
    with open('date', 'r') as f:
        for line in f:
            print(get_date(line))

main()