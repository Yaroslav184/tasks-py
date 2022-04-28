def main():
    with open('symbols', 'r') as f:
        symbols = f.read()
    with open('new_file', 'w') as f:
        f.write(symbols[::-1])

main()
print('Файл создан!')