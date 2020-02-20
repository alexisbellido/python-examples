import json
import requests

def process_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    # num = int(input("Enter a number\n"))
    # print(num * 2)
    # path = input("Enter a path\n")
    # print(path)

    path = 'luke.json'
    data = process_json(path)

    # print(json.dumps(data, indent=4))
    print(f"Name: {data['name']}")
