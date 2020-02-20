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
        # if (start_at < 2/21/2018 and end_at >)
        if (start_at == "2018-01-22T00:00:00-07:00" and end_at == "2018-02-21T23:59:59-07:00"):
            total_principal += payment['principal']
            # print(principal)
            # print(payment['loan']['borrower_id'])
            # print(payment['interest'])
            # print('====================')
            interest_per_borrower[payment['loan']['borrower_id']] += payment['interest']
        # break

    print("Total so far", total_principal)
    print(interest_per_borrower)
    max_interest = 0
    borrower_id = 0
    for id, interest in interest_per_borrower.items():
        print(id, interest)
        if interest > max_interest:
            max_interest = interest
            borrower_id = id

    print("max interest", max_interest)
    print("borrower_id", borrower_id)

    ################################

    for payment in payments:
        paid = int(payment['principal']) + int(payment['interest']) + int(payment['service_fee']['amount'])
        start_at = payment['period']['start_at']
        end_at = payment['period']['end_at']
        # if (start_at < 2/21/2018 and end_at >)
        if (payment['loan']['borrower_id'] == borrower_id):
            # total_principal += payment['principal']
            print(paid)
            print('====================')

    # print(json.dumps(payments, indent=4))
    # print(f"Name: {data['name']}")
