import requests
import json

parameters = {
    "price":0.8
    }
r = requests.get("http://www.boredapi.com/api/activity?", params=parameters)
j = r.json()
print(j)
