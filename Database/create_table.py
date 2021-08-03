import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="getaccess",
    database="petshop"
)


mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE petsnakes (name VARCHAR(20), breed VARCHAR(25),length float,description TEXT)")
