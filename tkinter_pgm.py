from tkinter import *
import pymysql


connection=pymysql.connect(host="localhost",user="root",password="oneteam",database="collegedb")

cursor=connection.cursor()

def add_dep():
    dep_name = dep.get()
    cursor.execute(f"INSERT INTO department (dp_name) VALUES ('{dep_name}')")
    connection.commit()
    dep.delete(0, END)

window=Tk()
Label(window,text="enter department name").grid(row=0,column=0)
dep=Entry(window)
dep.grid(row=0,column=1)
Button(window,text="save",command=add_dep).grid(row=1,column=0,columnspan=2)
window.mainloop()
