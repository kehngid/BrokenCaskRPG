from distutils.command.config import config
from InnCreation import *
from InnkeeperCreation import *
from datetime import datetime
import mysql.connector
from mysql.connector import Error

def NewGame():

    config = open('databaseConfig.txt', 'r')

    hostName = config.readline()
    databaseName = config.readline()
    userName = config.readline()
    passwordString = config.readline()

    connection = mysql.connector.connect(
        host = hostName,
        database = databaseName,
        user = userName,
        password = passwordString
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

    #Getting name 
    gameName = input("Name of New Game: ")
    #Getting datetime
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    #Inserting row into database
    sql = "INSERT INTO Game (Name, DateStarted, FKUserID) VALUES (%s, %s, %s)"
    val = (gameName,dt_string,"2")
    cursor.execute(sql,val)
    connection.commit()
    print(cursor.rowcount, "record inserted")

    #Getting UserID
    sql = "SELECT GameID FROM Game WHERE FKUserID = %s AND DateStarted = %s AND Name = %s;"
    val = ("2", dt_string, gameName)
    cursor.execute(sql,val)
    gameID = cursor.fetchall()
    print(gameID)

    #Prompt Inn creation
    Inn = InnCreation()


    #Prompt Innkeeper creation
    Innkeeper = InnkeeperCreation()

    #Prompt Employee creation

    if connection.is_connected():
        cursor.close()
    connection.close()
    print("MySQL connection is closed")
