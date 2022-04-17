import pytextnow as pytn
import os
from tercero import getTerceroDinner
from cuarto import getCuartoDinner
from segundo import getSegundoDinner
client = pytn.Client("rbudhiraja", sid_cookie = "SID_COOKIE", csrf_url = "CSRF_URL")

for filename in os.listdir("profiles"):
   with open(os.path.join("profiles", filename), 'r') as f:
        text = f.read()
        text = text.split(" ")
        if "3" in text and "a" in text:
            menu = getTerceroDinner()
            client.send_sms(text[0], "Dinner at Tercero DC today includes: ")
            client.send_sms(text[0], menu)
        if "3" in text and "b" in text:
            menu = getSegundoDinner()
            client.send_sms(text[0], "Dinner at Segundo DC today includes: ")
            client.send_sms(text[0], menu)
        if "3" in text and "c" in text:
            menu = getCuartoDinner()
            client.send_sms(text[0], "Dinner at Cuarto DC today includes: ")
            client.send_sms(text[0], menu)