import requests
import json
import time
from requests.auth import HTTPBasicAuth
email = "jccubero96@gmail.com "
password = "Chispa34"


response = requests.get("https://cubero.spaces.nexudus.com/api/spaces/coworkers", auth=(email,password))
cambiado =""
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
        i["Gender"]= 0
      #print i
        cambio = i


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
