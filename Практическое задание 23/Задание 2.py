def check_zero(numbers):
    for i in numbers:
        if i == 0:
            return True
    return False

if __name__ == '__main__':
    numbers = [int(i) for i in input('Введите числа через пробел: ').split()]
    print(check_zero(numbers))