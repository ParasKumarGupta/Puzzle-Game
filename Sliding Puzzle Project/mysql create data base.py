import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Paras7017")
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("create database logindb")
mycursor.execute("show databases")
for db in mycursor:
    print(db)

