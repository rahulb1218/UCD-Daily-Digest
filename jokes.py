import random
def getJoke():
    f = open("jokes.txt","r")
    lines = f.readlines()
    return random.choice(lines)