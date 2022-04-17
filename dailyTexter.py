import pytextnow as pytn
import os
from quote import getQuote
from jokes import getJoke
from weather import getWeather
from tercero import getTerceroBreakfast
from segundo import getSegundoBreakfast
from cuarto import getCuartoBreakfast
client = pytn.Client("rbudhiraja", sid_cookie="SID_COOKIE", csrf_cookie="CSRF_COOKIE")

for filename in os.listdir("profiles"):
   with open(os.path.join("profiles", filename), 'r') as f:
        text = f.read()
        text = text.split(" ")

        client.send_sms(text[0], "Good Morning!")
        if "2" in text:
            quote = getQuote()
            quote = quote.replace("\n", "")
            client.send_sms(text[0], quote)
        print(text[0])
        if "3" in text:
            joke = getJoke()
            joke = joke.replace("\n", "")
            list = joke.split("<>")
            client.send_sms(text[0], list[0])
            client.send_sms(text[0], "...")
            client.send_sms(text[0], list[1])
        if "1" in text: 
            weather = getWeather()
            client.send_sms(text[0], weather)
        if "4" in text and "a" in text:
            menu = getTerceroBreakfast()
            client.send_sms(text[0], "Breakfast at Tercero DC today includes: ")
            client.send_sms(text[0], menu)
        if "4" in text and "b" in text:
            menu = getSegundoBreakfast()
            client.send_sms(text[0], "Breakfast at Segundo DC today includes: ")
            client.send_sms(text[0], menu)
        if "4" in text and "c" in text:
            menu = getCuartoBreakfast()
            client.send_sms(text[0], "Breakfast at Cuarto DC today includes: ")
            client.send_sms(text[0], menu)

