def get_date(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]

def get_max_date(date_list):
    max_date = date_list[0]
    for date in date_list:
        if max_date < date:
            max_date = date
    return max_date

def main():
    date_list = get_date('text')
    max_date = get_max_date(date_list)
    print(max_date)

main()