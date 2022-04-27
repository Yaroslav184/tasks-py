def main():
    with open('text', 'r') as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    data = [x.split('-') for x in data]
    data = [(int(x[0]), int(x[1]), int(x[2])) for x in data]
    data = sorted(data)
    print(data[0])

main()