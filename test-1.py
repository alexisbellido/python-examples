import json
import requests


url = 'https://pokeapi.co/api/v2/pokemon/ditto'
response = requests.get(url)
data_api = json.loads(response.content.decode('utf8'))
# print(data_api)
print(data_api['abilities'])
print(json.dumps(data_api['abilities'], indent=4))

with open('luke.json') as json_file:
    data = json.load(json_file)
    # print(data)
    print(f"Name: {data['name']}")
