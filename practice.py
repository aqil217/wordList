import requests

api_key = '6e0fda1d-a131-4589-b337-8d8240179e51'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res = requests.get(url)
definitions = res.json()
for definition in definitions:
    print(definition)