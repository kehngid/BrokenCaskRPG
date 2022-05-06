from GeneralCharFunct import *
import random
import re

def RandClothing():
    return 'NULL'

def StatNum():
    x = random.randint(1,10)
    if x <= 4:
        return 1
    elif x <= 8:
        return 2
    else:
        return 3


# MAIN #
#-----------------------------------------------------------------------------#
def InnkeeperCreation():
    
    print("Randomized")
    name = RandName()
    print("Name: " + name)
    race = RandRace()
    print("Race: " + race)

    body = StatNum()
    mind = StatNum()
    heart = StatNum()

    print("Stats:")
    print("Body = " + str(body))
    print("Mind = " + str(mind))
    print("Heart = " + str(heart))

    return [name, race, body, mind, heart]