from functools import partial

primer = partial(int, base=2)
print(primer('1001000'))