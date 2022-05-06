import random
import re

def RandName():
    x1 = random.randint(1,6)
    y1 = random.randint(1,6)

    x2 = random.randint(1,6)
    y2 = random.randint(1,6)

    name1 = open('Tables/FirstName.txt', 'r')
    name2 = open('Tables/LastName.txt', 'r')
    
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

def RandRace():
    x = random.randint(2,12)

    races = open('Tables/Race.txt', 'r')

    line = races.readline()

    while(line):
        if(int(re.search(r'\d+', line).group()) == x):
            return line.split(';')[1]
        line = races.readline()

    return 'NULL'