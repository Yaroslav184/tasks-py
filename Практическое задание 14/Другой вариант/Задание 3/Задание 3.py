def read_file(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()
    return data

def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.writelines(data)

def find_min_price(data):
    min_price = int(input('Введите цену: '))
    for i in data:
        if int(i.split()[3]) < min_price:
            print(i)

def find_weight(data):
    weight = int(input('Введите вес: '))
    for i in data:
        if int(i.split()[2]) > weight:
            print(i)

def find_count(data):
    count = int(input('Введите количество: '))
    for i in data:
        if int(i.split()[1]) > count:
            print(i)

def main():
    data = read_file('baza')
    find_min_price(data)
    find_weight(data)
    find_count(data)
    write_file('baza', data)

main()