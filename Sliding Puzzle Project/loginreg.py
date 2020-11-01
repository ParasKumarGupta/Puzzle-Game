# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:24:03 2020

@author: HP
"""

#importing modules
from tkinter import *
import tkinter.messagebox
import mysql.connector


#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="Paras7017",database="logindb")
cursordb = connectiondb.cursor()


def register():
        global root3 #making new root window for registering the account details
        root3=Tk()
        root3.geometry("400x400")
        root3.title("Account Register")
        root3.configure(bg="red") 
        global username
        global password
        username= StringVar(root3)
        password= StringVar(root3)
        Label(root3, text='Please Enter your Account Details', bd=8,font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
        Label(root3, text="",bg="red").pack()
        Label(root3, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root3, textvariable=username, bd=1,relief="solid").pack()
        Label(root3, text="",bg="red").pack()
        Label(root3, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root3, textvariable=password, show="*", bd=1,relief="solid").pack()
        Label(root3, text="",bg="red").pack()
        Button(root3, text="Register", bg="blue", fg='white',bd=8, relief="groove", font=('arial', 12, 'bold'),command=savedata).pack()
        Label(root3, text="",bg="red")
        
        
        
def savedata():
        v1 =username.get() #getting values from entry data in register
        v2= password.get()
        #inserting entry data to the Mysql database
        cursordb.execute("insert into usertable values('{0}','{1}')".format(v1,v2))
        connectiondb.commit()         
        print(cursordb.rowcount, "details inserted")
        root3.destroy()
        return

def login():
    global root2
    root2 = Toplevel(root) #making new root window for login
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")

    global username_verification
    global password_verification
    Label(root2, text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_verification).pack()
    Label(root2, text="")

def logged_destroy():
    logged_message.destroy() #destroying all window after successfully login and starting game
    root2.destroy()
    root.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message #login successfully root window
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    # used string interpolation to get the username_verification value
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Start The Game", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()


def failed():
    global failed_message #when the user input wrong entry in login then this root window will be there to show
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()


def login_verification():
    user_verification = username_verification.get() #checking the user account details in database and verifying  
    pass_verification = password_verification.get()
    sql = "select * from usertable where username = %s and password = %s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def Exit():
    #if user doesnt want to login and register then he directed to the game
    wayOut = tkinter.messagebox.askyesno("Login and Register System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

def main_display():
    global root# displaying 1st window when the main file is executed
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("800x400")
    Label(root,text='Welcome to Log In and Register System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=login).pack()
    Label(root,text="").pack()
    Button(root, text = "Register",bg="blue", command = register,bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white"
                   ,width=20).pack()

    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Exit).pack()
    Label(root,text="").pack()

main_display()
root.title("Login And Register form")

root.mainloop()
