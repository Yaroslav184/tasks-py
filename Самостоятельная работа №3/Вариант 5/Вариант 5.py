def get_min_date(file_name):
    with open(file_name, 'r') as f:
        dates = f.readlines()
        min_date = dates[0]
        for date in dates:
            if date < min_date:
                min_date = date
        return min_date

if __name__ == '__main__':
    print(get_min_date('date'))