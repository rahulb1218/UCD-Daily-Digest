
import pytextnow as pytn
client = pytn.Client("rbudhiraja", sid_cookie = "SID_COOKIE", csrf_url = "CSRF_URL")
intro = "Hello! My name is UCD Daily Digest. I am your personal daily wellness assistant. I can talk to you about many things. Here are some things I can text you about:"
items  = "[1] Weather, [2] Daily Motivational Quote, [3] Jokes, and [4] Dining Hall Menus: [a] Tercero, [b] Segundo, [c] Cuarto"
itemList = []
from tercero import getTerceroBreakfast
from segundo import getSegundoBreakfast
from cuarto import getCuartoBreakfast
from tercero import getTerceroLunch
from segundo import getSegundoLunch
from cuarto import getCuartoLunch
from tercero import getTerceroDinner
from segundo import getSegundoDinner
from cuarto import getCuartoDinner

@client.on("message")
def handler(msg):
    if msg.type == pytn.MESSAGE_TYPE:
        print("got message")
        input = msg.content.split(" ")
        if msg.content.lower() == "setup":
            msg.send_sms(intro)
            msg.send_sms(items)
            msg.send_sms("Which of these would you like to have daily notifications for and which is your primary DC? Please enter the numbers and letter separated by a single space. Example:")
            msg.send_sms("1 4 a")
            msg.send_sms("If you would like to not subscribe to any notifications and just want to see menus, please reply with a 0.")
        if input[0].isnumeric() and msg.content != "0":
            profile = ""
            f = open("/Users/rahul/Documents/GitHub/hackDavis2022/profiles/" + str(msg.number), "w")
            profile += str(msg.number) + " "
            for i in range(len(input)):
                profile += input[i] + " "
            f.write(profile)
            msg.send_sms("Great, thanks for using UCD Daily Digest! You will receive your morning digest at 6am each day for what you're subscribed to and menus an hour before breakfast/lunch/dinner start if you opted for them.")
            msg.send_sms("Also, you can get any menu at anytime by using the following commands: DC_name meal. For example: tercero lunch or segundo dinner")
        if msg.content == "0":
            msg.send_sms("You can get any menu at anytime by using the following commands: DC_name meal. For example: tercero lunch or segundo dinner")
        if msg.content.lower() == "segundo breakfast":
            menu = getSegundoBreakfast()
            msg.send_sms("Breakfast at Segundo DC today includes: ")
            msg.send_sms(menu)
        if msg.content.lower() == "segundo lunch":
            menu = getSegundoLunch()
            msg.send_sms("Lunch at Segundo DC today includes: ")
            msg.send_sms(menu)
        if msg.content.lower() == "segundo dinner":
            menu = getSegundoDinner()
            msg.send_sms("Dinner at Segundo DC today includes: ")
            msg.send_sms(menu)
        if msg.content.lower() == "cuarto breakfast":
            menu = getCuartoBreakfast()
            msg.send_sms("Breakfast at Cuarto DC today includes: ")
            msg.send_sms(menu)
        if msg.content.lower() == "cuarto lunch":
            menu = getCuartoLunch()
            msg.send_sms("Lunch at Cuarto DC today includes: ")
            msg.send_sms(menu)
        if msg.content.lower() == "cuarto dinner":
            menu = getCuartoDinner()
            msg.send_sms("Dinner at Cuarto DC today includes: ")
            msg.send_sms(menu)
        if msg.content.lower() == "tercero breakfast":
            menu = getTerceroBreakfast()
            msg.send_sms("Breakfast at Tercero DC today includes: ")
            msg.send_sms(menu)
        if msg.content.lower() == "tercero lunch":
            menu = getTerceroLunch()
            msg.send_sms("Lunch at Tercero DC today includes: ")
            msg.send_sms(menu)
        if msg.content.lower() == "tercero dinner":
            menu = getTerceroDinner()
            msg.send_sms("Dinner at Tercero DC today includes: ")
            msg.send_sms(menu)
