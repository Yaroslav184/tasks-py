def main():
    with open('input', 'r') as f:
        data = f.readlines()
    for i in data:
        a, b, c = i.split()
        a, b, c = int(a), int(b), int(c)
        if a + b == c:
            print(a)
            break
    else:
        print(0)

main()