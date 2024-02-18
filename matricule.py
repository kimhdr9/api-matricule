import requests
import json
hostname="https://apiplaqueimmatriculation.com"
immatriculation="EJ-941-ZH"
immatriculation="CY-648-SH"
immatriculation="AC-471-VF"

print('Entrer le matricule avec le format AB-123-CD')
immatriculation= input()

token='TokenDemo'
format='json'
api_url="http://api.apiplaqueimmatriculation.com/get-vehicule-info?host_name="+hostname+"&immatriculation="+immatriculation+"&token="+token+"&format="+format

response=requests.get(api_url)

# print(response.json())

brut=response.json()
dico=brut['data']

for key,value in dico.items():
    print(f'{key} : {value}')
