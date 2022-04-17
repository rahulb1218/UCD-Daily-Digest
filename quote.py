import random
def getQuote():
    f = open("quotes.txt","r")
    lines = f.readlines()
    return random.choice(lines)