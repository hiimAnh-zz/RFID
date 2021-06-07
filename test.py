import requests

url = 'http://192.168.1.191:8181/log'
headers = {'sguid':'2ce81521-c42f-4556-8c28-c69d7e3a3a47','rfid-tag' : '0x4E 0x7E 0xDD 0xB3'}

x = requests.post(url,data= 'aaa', headers = headers)


print(x.text)
