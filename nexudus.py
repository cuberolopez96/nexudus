import requests
import json
import time
from requests.auth import HTTPBasicAuth
email = "email"
password = "password"


response = requests.get("https://cubero.spaces.nexudus.com/api/spaces/coworkers", auth=(email,password))

if response.status_code == 200:
  #print response.text
  aux =""
  #print response.status_code
  resultado = response.json()
  array = json.dumps(resultado)
  datos = json.loads(array)
  #print "\n/////////////////////\nDATOS INICIALES\n///////////////////\n"
  #print array
  for i in datos["Records"]:
    print "//////////////////ciclo for//////////////////////"
   # print a
   # print i
    if i["Email"] == "jccubero96@gmail.com":
      #print i
      cambio= {
        "Id": i["Id"],
        "FullName": "Paquito",
        "Email": "jccubero96@gmail.com",
        "CountryId": 789456,
        "SimpleTimeZoneId": 789456,
        "CheckinSinceLastRenewal": 0,
        "MinutesSinceLastRenewal": 0,
        
      }


      aux=cambio



      print "////////////////////////aux////////////////////////////"
      print aux
 # print "/////////////////////////////////////////////////////"
#print i
    #aux = aux + json.dumps(i)
cambiado = json.dumps(aux)
#cambiado = json.loads(cambiado)
print cambiado

change = requests.put("https://cubero.spaces.nexudus.com/api/spaces/coworkers", data = cambiado, auth=(email,password), headers={'Content-type':'application/json'})
if change.status_code == 500:
  print "Error 500!"
else:
  print change.status_code
  print change.json()
  print change.content

result = requests.get("https://cubero.spaces.nexudus.com/api/spaces/coworkers", auth=(email,password))
if result.status_code==200:
    result =  result.json()
    result = json.dumps(result)
    result = json.loads(result)
    for resultado in result['Records']:
        print resultado["Custom1"]

#fc126d4723fb40f999b2bac5256c2278
