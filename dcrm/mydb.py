import mysql.connector

# define database
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd  = 'Password123',
)

# prepare a cursor object 
cursorObject = database.cursor()

# create database
cursorObject.execute("CREATE DATABASE modnationgamers")

print("ALL DONE")