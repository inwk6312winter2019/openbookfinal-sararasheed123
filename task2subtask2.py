 Import requests library
import requests


import json

url = 'https://{APIC-EM-Controller}/api/v1/ticket/ip'

header = {"content-type": "application/json/ip"}


response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

print(response.text)
