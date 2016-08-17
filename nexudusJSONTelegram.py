import requests
import json
NEXUDUS_EMAIL=""
NEXUDUS_PASSWORD = ""


banderas = []
def recogercoworkers() :
    response = requests.get("https://cubero.spaces.nexudus.com/api/spaces/coworkers", auth=(NEXUDUS_EMAIL,NEXUDUS_PASSWORD))

    coworkers = response.json()
    coworkers = json.dumps(coworkers)
    coworkers = json.loads(coworkers)
    return coworkers
def actualizardatos() :
    with open('coworkers.json','r') as archivo:
        archivo1= archivo.read()
        coworkersjson = json.loads(archivo1)
        coworkers = recogercoworkers()
        nuevojson={}
        i= 0;
        for coworker in coworkers['Records']:
            data = {
                'Nombre':coworker['FullName'],
                'Email':coworker['Email']
            }
            nuevojson[i]=data
            i=i+1
        with open('coworkers.json','w+') as archivonuevo:
            archivonuevo.write(json.dumps(nuevojson))
while True:
    actualizardatos()
