#create a table:
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Paras7017",database="logindb")
mycursor=mydb.cursor()
#mycursor.execute("create table usertable (username varchar(20),password varchar(30))")
mycursor.execute("show tables")
for tb in mycursor:
 print(tb)
