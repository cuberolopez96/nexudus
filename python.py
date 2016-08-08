import requests
import json
import time
from requests.auth import HTTPBasicAuth
email = "empireofjuan001@hotmail.com"
password = "password"


response = requests.get("https://kalujas.spaces.nexudus.com/api/spaces/coworkers", auth=Auth)

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
    if i["Email"] == "i62seroj@uco.es":
      #print i
      print i["Custom1"]
      i["Custom1"] = "prueba"
      aux = i
      #print aux
 # print "/////////////////////////////////////////////////////"
#print i    
    #aux = aux + json.dumps(i) 
cambiado = json.dumps(aux) 
#cambiado = json.loads(cambiado)
#print cambiado

change = requests.put("https://kalujas.spaces.nexudus.com/api/spaces/coworkers", data = cambiado, auth=(email,password), headers={'Content-type':'application/json'})
if change.status_code == 500:
  print "Error 500!"
else:
  print change.status_code
  print change.json();
  print change.content

#fc126d4723fb40f999b2bac5256c2278
