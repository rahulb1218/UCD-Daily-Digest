import string
from xml.dom.minidom import Document
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
stringFood =  ""
dayCount = 1
meal = 3
print(stringFood)
url = 'https://housing.ucdavis.edu/dining/menus/dining-commons/tercero/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
from datetime import datetime
theDay = datetime.today().weekday()

if theDay == 6:
    day = 1
else:
    theDay += 2

def getTerceroBreakfast():
    breakfast = ""
    whatDay = "tab" + str(theDay) + "content"
    divs = soup.find_all("div", {"id": whatDay})
    theDiv = divs[0].findChildren(recursive=False) #0 will not change, array of length 1
    for span in theDiv[2].select("span"):#Breakfast is 2, 3 is lunch, 4 is dinner
        breakfast += str(span)
        breakfast += ", "
        breakfast = breakfast.replace("<span>", "")
        breakfast = breakfast.replace("</span>", "")
    return breakfast

def getTerceroLunch():
    lunch = ""
    whatDay = "tab" + str(theDay) + "content"
    divs = soup.find_all("div", {"id": whatDay})
    theDiv = divs[0].findChildren(recursive=False) #0 will not change, array of length 1
    for span in theDiv[3].select("span"):#lunch is 2, 3 is lunch, 4 is dinner
        lunch += str(span)
        lunch += ", "
        lunch = lunch.replace("<span>", "")
        lunch = lunch.replace("</span>", "")
    return lunch

def getTerceroDinner():
    dinner = ""
    whatDay = "tab" + str(theDay) + "content"
    divs = soup.find_all("div", {"id": whatDay})
    theDiv = divs[0].findChildren(recursive=False) #0 will not change, array of length 1
    for span in theDiv[4].select("span"):#dinner is 2, 3 is dinner, 4 is dinner
        dinner += str(span)
        dinner += ", "
        dinner = dinner.replace("<span>", "")
        dinner = dinner.replace("</span>", "")
    return dinner