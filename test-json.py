import json
import requests

def process_json():
    url = 'https://pokeapi.co/api/v2/pokemon/ditto'
    response = requests.get(url)
    data_api = json.loads(response.content.decode('utf8'))
    # print(data_api)
    # print(json.dumps(data_api, indent=4))
    # print(data_api['abilities'])
    print(json.dumps(data_api['abilities'], indent=4))

    with open('luke.json') as json_file:
        data = json.load(json_file)
        # print(data)
        # print(json.dumps(data, indent=4))
        print(f"Name: {data['name']}")

if __name__ == '__main__':
    process_json()
