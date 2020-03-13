import json
# import requests

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

    for payment in payments:
        principal = int(payment['principal'])
        start_at = payment['period']['start_at']
        end_at = payment['period']['end_at']
        print(start_at)
        break
