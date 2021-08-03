import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="getaccess"
)

mycursor = mydb.cursor()

#create database 
mycursor.execute("CREATE DATABASE mydatabase") #mydatabase=nameofdatabase
