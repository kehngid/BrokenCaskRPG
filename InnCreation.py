import random
import re

def RandInnName():
    x1 = random.randint(1,6)
    y1 = random.randint(1,6)

    x2 = random.randint(1,6)
    y2 = random.randint(1,6)

    name1 = open('Tables/InnName1.txt', 'r')
    name2 = open('Tables/InnName2.txt', 'r')
    
    nameNum = [x1 * 10 + y1, y1 * 10 + x1, x2 * 10 + y2, y2 * 10 + x2]

    print(nameNum)

    #Getting names from InnName1.txt 
    firstName = ['', '']
    line = name1.readline()
    count = 0

    while(line):
        if(int(re.search(r'\d+', line).group()) == nameNum[0] or int(re.search(r'\d+', line).group()) == nameNum[1]):
            firstName[count] = line.split(',')[1]
            count = count + 1
        line = name1.readline()
    #print(firstName)

    #Getting names from InnName2.txt
    lastName = ['', '']
    line = name2.readline()
    count = 0

    while(line):
        if(int(re.search(r'\d+', line).group()) == nameNum[2] or int(re.search(r'\d+', line).group()) == nameNum[3]):
            lastName[count] = line.split(',')[1]
            count = count + 1
        line = name2.readline()
    #print(lastName)
    
    nameOptions = [firstName[0] + ', ' + lastName[0], firstName[0] + ', ' + lastName[1], firstName[1] + ', ' + lastName[0], firstName[1] + ', ' + lastName[1]]
    
    #print(nameOptions)

    name1.close()
    name2.close()

    print("Inn Names: ")
    print(nameOptions[0])
    print(nameOptions[1])
    print(nameOptions[2])
    print(nameOptions[3])
    userInput = input("Please pick your name (type the name you want): ")
    
    return userInput

def RandInnLocation():
    x = random.randint(2,12)

    location = open('Tables/InnLocation.txt', 'r')

    line = location.readline()

    while(line):
        if(int(re.search(r'\d+', line).group()) == x):
            return line.split(',')[1]
        line = location.readline()

    return 'NULL'

def RandInnApperance():
    x = random.randint(2,12)

    apperance = open('Tables/InnApperance.txt', 'r')

    line = apperance.readline()

    while(line):
        if(int(re.search(r'\d+', line).group()) == x):
            return line.split(';')[1]
        line = apperance.readline()

    return 'NULL'

def RandInnType():
    x = random.randint(2,12)

    type = open('Tables/InnType.txt', 'r')
    typearr = ['', '']

    line = type.readline()

    while(line):
        if(int(re.search(r'\d+', line).group()) == x):
            typearr[0] = line.split(';')[1]
            typearr[1] = line.split(';')[2]
        line = type.readline()

    return typearr

def RandSigDrink():
    x = random.randint(2,12)

    sigdrink = open('Tables/SigDrink.txt', 'r')

    line = sigdrink.readline()

    while(line):
        if(int(re.search(r'\d+', line).group()) == x):
            return line.split(';')[1]
        line = sigdrink.readline()

    return 'NULL'

# MAIN #
#-----------------------------------------------------------------------------#
def InnCreation():

    print("Randomized")
    InnName = RandInnName()
    print("Inn Name: " + InnName)
    InnLocation = RandInnLocation()
    print("Inn Location: " + InnLocation)
    InnApperance = RandInnApperance()
    print("Inn Apperance: " + InnApperance)
    InnType = RandInnType()
    print("Inn Type: " + InnType[0])
    print("Inn Guest Type: " + InnType[1])
    InnSigDrink = RandSigDrink()
    print("Inn Signature Drink: " + InnSigDrink)

    return [InnName, InnLocation, InnApperance, InnType[0], InnType[1], InnSigDrink]


