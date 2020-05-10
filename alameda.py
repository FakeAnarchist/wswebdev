import requests
import json

r=requests.get("https://fenix.tecnico.ulisboa.pt/api/fenix/v1/parking")

if(r.ok):
    y=(json.loads(r.content)).get("Alameda").get("freeSlots")
    print("there are ",y," slots available")
    