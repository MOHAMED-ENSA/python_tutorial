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

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="db2"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECt * FROM students")
# for x in mycursor : 
#   print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="db2"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECt id,name FROM students")
# for x in mycursor : 
#   print(x)
# use fetchone method 
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="db2"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECt * FROM students")
# res = mycursor.fetchone()
# print(res)

# write a function which print specific rows 

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="12345",
#   database="db2"
# )

# mycursor = mydb.cursor()
# def printSpeceficRows(min,max) :
#   mycursor.execute("SELECt id,name FROM students")
#   a = 0 
#   while  a < max   : 
#      res = mycursor.fetchone()
#      a += 1
#      if a >= min and a <= max :
#          print(res) 

# printSpeceficRows(3,7)

# where / fetch all : 
# import mysql.connector as mc 
# mybd = mc.connect(
#   host="localhost" , 
#   user = "root" , 
#   passwd = "12345", 
#   database = "db2"
# )
# mycursor = mybd.cursor() 
# ids = (1,2,3,4,5,6)

# mycursor.execute(f'SELECT CNE FROM students WHERE id in {ids} and name = "Mohamed" ')
# res = mycursor.fetchall()
# print(res)

# using where whith regular expretion 
# import mysql.connector as mc 
# mybd = mc.connect(
#   host="localhost" , 
#   user = "root" , 
#   passwd = "12345", 
#   database = "db2"
# )
# mycursor = mybd.cursor() 

# mycursor.execute('SELECT * FROM students WHERE class LIKE "%G%"  ')
# res = mycursor.fetchall()
# print(res)

# insert using oop : 
# from oop import students 
# import mysql.connector as mc
# print("-" * 40) 
# std1 = students("Kamal",1314247688,"GIND4")


# mydb = mc.connect(
#     host ="localhost",
#     user = "root",
#     passwd ="12345",
#     database = "db2"
# )
# mycursor = mydb.cursor()
# mycursor.execute("INSERT INTO students (name,CNE,class) VALUES (%s,%s,%s)",(std1.name,std1.CNE,std1.Class))
# mydb.commit()
# print("%s recrods added",mycursor.rowcount)
# create table + oop 

# from oop import students 
# import mysql.connector as mc
# std1 = students("Houda",1314446878,"GC4")
# std2 = students("Souad",1314544448,"GE3")
# std3 = students("Soufian",1344464688,"GSEIR5")
# std4 = students("Sara",1314122688,"GI3")
# print("-" * 40) 
# mydb = mc.connect(
#     host ="localhost",
#     user = "root",
#     passwd ="12345",
#     database = "mydb2"
# )
# mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE students (id INT ,name VARCHAR(255),CNE INT,Class VARCHAR(255))")
# info = [(std1.id,std1.name,std1.CNE,std1.Class),
#         (std2.id,std2.name,std2.CNE,std2.Class) 
#          ]
# print(info)
# sql = "INSERT INTO students (id,name,CNE,Class) VALUES (%s,%s,%s,%s)"
# mycursor.executemany(sql,info)
# mydb.commit()
# print(mycursor.rowcount , " recrods added")

# order by : 


