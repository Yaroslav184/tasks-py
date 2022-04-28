def main():
    print('Числа возведенные в квадрат:')
    with open('file', 'r') as file:
        for line in file:
            print(int(line) ** 2)

main()