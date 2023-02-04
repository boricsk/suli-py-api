#genderize.io
import requests

def getGender(name):
    URL1 = 'https://api.genderize.io/'
    payload = {'name':name}
    resp = requests.get(URL1, params=payload)
    valoszinuseg = resp.json()['probability']
    nem = resp.json()['gender']
    return valoszinuseg, nem #tuple formában fog visszatérni

def getAge(name):
    URL2 = 'https://api.agify.io/'
    payload = {'name':name}
    respAge = requests.get(URL2, params=payload)
    return respAge.json()['age']

def getNational(name):
    URL3 ='https://api.nationalize.io/'
    payload = {'name':name}
    respNat = requests.get(URL3, params=payload)
    nat = respNat.json()['country']
    for items in nat:
        print(f'Az ország : {items["country_id"]} , a valószínűség : {items["probability"] * 100:.0f}%')
    
    

print('A keresztnév alapján kitalálom a nemedet, korodat és az országodat.')
nev = input('Add meg a nevet :')

payload = {'name':nev}

print(f'{getGender(nev)[0] * 100:.0f}%-os valószínűséggel a {nev} név az {"férfi." if getGender(nev)[1] == "male" else "nő."} A becsült kor {getAge(nev)} év.')
getNational(nev)
#32:26