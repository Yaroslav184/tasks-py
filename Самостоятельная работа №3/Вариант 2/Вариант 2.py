def main():
    with open('Действительные числа', 'r') as f:
        lines = f.readlines()
        lines = [int(line.strip()) for line in lines]
        print(f'Сумма наибольшего и наименьшего значений: {min(lines) + max(lines)}')

main()