# this is a tutorial about how to connect python to mysql server
# get started 
# establish commincation 

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345"
# )

# print(mydb)
# create database 
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# check if it exists
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

# create a table 
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# check if it exists : 
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# create automatic primary key 

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# if the table already exist use the following code :  
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
 
# fill a table  : 
# import mysql.connector as mc 

# mydb = mc.connect(
#   host = "localhost",
#   user = "root",
#   passwd ="12345",
#   database = "db2"
# )
# mycursor = mydb.cursor()

# sql = "INSERT INTO students (name,CNE,class) VALUES (%s,%s,%s)"
# exit = ""
# col = 0 
# while(exit != "exit") :
#     name = input("enter your name :  ")
#     CNE = int(input("enter your CNE :  "))
#     Class = input("enter your class :  ")
#     values  = (name,CNE,Class)
#     mycursor.execute(sql,values)
#     mydb.commit()
#     exit = input("write exit to exit")
#     col += 1 

# #print(mycursor.rowcount , "record inserted")
# print(f"{col} columns added ")

# get the id for the the row added : 
# import mysql.connector as mc
# mydb = mc.connect(
#   host = "localhost",
#   user = "root",
#   passwd ="12345",
#   database = "db2"
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO students (name,CNE,class) VALUES (%s,%s,%s)"
# values  = ("soufian","1324567894","GI4")
# mycursor.execute(sql,values)
# mydb.commit()
# print(mycursor.rowcount , "record inserted")
# #print(f"{col} columns added ")

# print("id value for column added is : ", mycursor.lastrowid)

# select from a table : 

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345",
  database="db2"
)

mycursor = mydb.cursor()
mycursor.execute("SELECt * FROM students")
for x in mycursor : 
  print(x)






