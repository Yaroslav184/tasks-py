from math import gcd
from random import randint

class Fraction:
    def __init__(self, number, divider):
        if number != 0 and divider != 0:
            k = gcd(number, divider)
            self.number = number // k
            self.divider = divider // k

    def __str__(self):
        return f'{self.number}/{self.divider}'

    def __repr__(self):
        return f'{self.number}/{self.divider}'

    def __mul__(self, other):
        return Fraction(self.number * other, self.divider)

    def __div__(self, other):
        if other == 0:
            return
        return Fraction(self.number, self.divider * other)

fraction = [Fraction(randint(1, 5), randint(1, 5)) for i in range(10)]

for f in fraction:
    n = randint(1, 10)
    print(f'{f} * {n} = {f.__mul__(n)}')
    print(f'{f} / {n} = {f.__div__(n)}')
