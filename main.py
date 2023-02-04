import requests
'''

resp = requests.get('https://sulipy.hu/')

print(resp) #ebben az esetben csak a szerver válaszkód lesz látható.
print(type(resp))

#objektum információinak lekérése
#print(dir(resp))
#print(help(resp))

#a válasu kiirása byte és text formában
print(resp.content)
print(resp.text)

#Kép letöltése egy oldarról

resp = requests.get('https://tryhackme-images.s3.amazonaws.com/user-uploads/62c435d1f4d84a005f5df811/room-content/beb65f89b68c9b9123a81d670ac39241.png')

with open('advent.png', 'wb') as kimenet:
    kimenet.write(resp.content)

'''
#API-k kezelése. Egy olyan oldalt fogunk használni, ami macskákról közöl információkat

resp = requests.get('https://catfact.ninja/fact') #Ez az API cime
print(resp.json()) #JSON formátumú string lesz a válasz, konvenrálás szórárrá.
fact = resp.json()['fact']
print(fact)

