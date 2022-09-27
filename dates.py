import json
# import requests
from datetime import datetime, date, time, timedelta


def process_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    # num = int(input("Enter a number\n"))
    # print(num * 2)
    # path = input("Enter a path\n")
    # print(path)

    path = 'data.json'
    payments = process_json(path)

    total_principal = 0
    interest_per_borrower = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    }

    test_dt = datetime(2020, 3, 13, hour = 23, minute = 30)
    print(test_dt)
    print('=====')

    test_date = date(2009, 3, 6)
    print(test_date)
    print('weekday', test_date.weekday())
    print(test_date.ctime())
    print('=====')

    # for payment in payments:
    for i, payment in enumerate(payments):
        principal = int(payment['principal'])
        start_at = payment['period']['start_at']
        end_at = payment['period']['end_at']
        print(i, ': start_at', start_at)
        the_start_date = datetime.fromisoformat(start_at)
        print('the_start_date', the_start_date)
        print('YYYY MM DD', the_start_date.year, the_start_date.month, the_start_date.day)
        print('------')
        if i == 5:
            break

    date_from_ts = date.fromtimestamp(228282)
    print('===', date_from_ts)
    now = datetime.now()
    print('now YYYY MM DD', now, now.year, now.month, now.day)
    print(now.strftime('Using strftime: %A, %Y-%m-%d'))

    one_year = timedelta(days=365)
    day_next_year = now + one_year
    print('same day next year', day_next_year)
