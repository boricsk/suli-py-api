#https://github.com/Hipo/university-domains-list-api

import requests

URL = 'http://universities.hipolabs.com/search'
payload ={'country':'hungary', 'name':'budapest'}

resp = requests.get(URL, params=payload)
egyetemek = resp.json()

for egyetem in egyetemek:
    print(egyetem)

print(resp.url)