import json
from datetime import datetime, date, time, timedelta
import sys
import pprint


def process_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data

def locate(data, state_to_locate):
    spots = []
    for parking_spot in data:
        state = parking_spot['address']['state']
        if state == state_to_locate:
            spots.append(parking_spot["name"])
    return spots

    # for key, value in person.items():
    #     print(key, value)

    return []

def find_price_hourly_lte(data, price_in_cents):
    spots = []
    price_in_cents = int(price_in_cents)
    for parking_spot in data:
        price_hourly = parking_spot['price_hourly']
        if price_hourly <= price_in_cents:
            spots.append(parking_spot["name"])
    return spots

def find_price_hourly_gt(data, price_in_cents):
    spots = []
    price_in_cents = int(price_in_cents)
    for parking_spot in data:
        price_hourly = parking_spot['price_hourly']
        if price_hourly > price_in_cents:
            spots.append(parking_spot["name"])
    return spots


if __name__ == '__main__':

    # python3 parkbot.py data.json locate AZ

    try:
        filename = sys.argv[1]
        command = sys.argv[2]
    except IndexError:
        print("Your command is invalid.")
        sys.exit()

    data = process_json(filename)

    if command == 'locate':
        state = sys.argv[3]
        spots_located = locate(data, state)
        pprint.pprint(spots_located)

    if command == 'find_price_hourly_lte':
        price = sys.argv[3]
        spots_located = find_price_hourly_lte(data, price)
        pprint.pprint(spots_located)

    if command == 'find_price_hourly_gt':
        price = sys.argv[3]
        spots_located = find_price_hourly_gt(data, price)
        pprint.pprint(spots_located)
