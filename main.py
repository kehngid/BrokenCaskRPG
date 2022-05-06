from NewGame import *
from ContinueGame import *
from Option import *
import re
import mysql.connector

#Menu Display
cont = 1

while(cont):
    print("[1] New Game")
    print("[2] Continue Game")
    print("[3] Options")
    print("[4] Exit game")
    print()

    userInput = input("User Input: ")
    print()

    if(userInput == "1"):
        NewGame()
    elif(userInput == "2"):
        ContinueGame()
    elif(userInput == "3"):
        Option()
    elif(userInput == "4"):
        cont = 0
    else:
        print("Not an option")

    print()


