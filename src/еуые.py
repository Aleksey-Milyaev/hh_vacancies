import requests
import json

url = "https://api.hh.ru/vacancies"
params = {'text': "python", 'page': 1, 'per_page': 100}

response = requests.get(url, params=params)
print(len(json.loads(response.text)["items"]))