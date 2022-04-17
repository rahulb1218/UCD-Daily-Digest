import pytextnow as pytn
import os
from tercero import getTerceroBreakfast
from cuarto import getCuartoBreakfast
from segundo import getSegundoBreakfast
client = pytn.Client("rbudhiraja", sid_cookie = "SID_COOKIE", csrf_url = "CSRF_URL")

for filename in os.listdir("profiles"):
   with open(os.path.join("profiles", filename), 'r') as f:
        text = f.read()
        text = text.split(" ")
        if "3" in text and "a" in text:
            menu = getTerceroBreakfast()
            client.send_sms(text[0], "Breakfast at Tercero DC today includes: ")
            client.send_sms(text[0], menu)
        if "3" in text and "b" in text:
            menu = getSegundoBreakfast()
            client.send_sms(text[0], "Breakfast at Segundo DC today includes: ")
            client.send_sms(text[0], menu)
        if "3" in text and "c" in text:
            menu = getCuartoBreakfast()
            client.send_sms(text[0], "Breakfast at Cuarto DC today includes: ")
            client.send_sms(text[0], menu)