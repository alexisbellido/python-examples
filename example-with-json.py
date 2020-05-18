import json
from datetime import datetime, date, time, timedelta

def process_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    # num = int(input("Enter a number\n"))

    path = 'data.json'
    data = process_json(path)

    for line in data:
        print(line['loan']['id'], line['loan']['amount'])
        break

    person = {
        'name': 'Pete',
        'age': 24,
    }
    for key, value in person.items():
        print(key, value)
    


