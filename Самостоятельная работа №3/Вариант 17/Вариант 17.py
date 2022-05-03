def sum_and_product():
    with open('file', 'r') as f:
        sum_ = 0
        mult = 1
        for line in f:
            sum_ += int(line)
            mult *= int(line)
        print(f'Сумма чисел: {sum_}')
        print(f'Произведение чисел: {mult}')

sum_and_product()