import tkinter
import calendar
from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="jitusamar0929",database="activity")


# functions for database---------------------------------------------------------------------------------------------------------------------------

def show():
    mycursor = mydb.cursor()
    mycursor.execute("select * from work")
    myresult = mycursor.fetchall()
    for x in myresult:
     print(x)


def savedata():
    mycursor = mydb.cursor()
    # mycursor.execute("create database activity")
    # mycursor.execute("create table work(dates int(10),days varchar(50),descriptions varchar(60))")
    mycursor.execute("insert into work values(%s,%s,%s)", (date.get(), day.get(), des.get()))
    mydb.commit()
    messagebox.showinfo("Info","Your data is saved successfully")


# function for display calendar---------------------------------------------------------------------------------------------------------------------

def showcalendar():
    cal=tkinter.Tk()
    cal.geometry("400x400")
    cal.title("Calendar")
    cal.configure(bg="white")
    year1=int(search1.get())
    month1=int(search2.get())

    fetch1=calendar.month(year1,month1)
    l3=Label(cal,text=fetch1,font=("Helvetica",10,"bold"))
    l3.pack(fill="both")


    cal.mainloop()


#main window for inputs------------------------------------------------------------------------------

root=tkinter.Tk()
root.title("Calendar")
root.geometry("600x600")
root.configure(bg="light blue")
lb1=tkinter.Label(root,text="GUI Calendar",bg="green",font=("Helvetica",30,"bold"))
lb1.pack(fill="both")

lb2=tkinter.Label(root,text="Enter year you want to see",bg="brown",font=("Bodoni",12))
lb2.pack()
search1=tkinter.Entry(root,bd=5,fg="blue",font=("Bodoni",15))
search1.pack(pady=5)
lb4=tkinter.Label(root,text="Enter month",bg="brown",font=("Bodoni",12))
lb4.pack()
search2=tkinter.Entry(root,bd=5,fg="blue",font=("Bodoni",15))
search2.pack(pady=5)

btn1=tkinter.Button(root,text="Exit",bg="red",font=("Bodoni",12),command=exit)
btn2=tkinter.Button(root,text="Show calendar",bg="red",font=("Bodoni",12),command=showcalendar)
btn2.pack()
btn1.pack(pady=5)


# inputs for database----------------------------------------------------------------------------------------------------------------------------
rem=Label(root,text="Reminder",font=("Bodoni",12),bg="orange")
rem.pack(pady=8)
date = IntVar()
day = StringVar()
des = StringVar()

j=Label(root,text="enter date",bg="brown",font=("Bodoni",12))
j.place(x=150,y=303)
d = Entry(root,textvariable=date,bd=5,fg="blue",font=("Helvetica",12))
d.place(x=235,y=300)

i=Label(root, text="enter day",bg="brown",font=("Bodoni",12))
i.place(x=150,y=340)
da = Entry(root,textvariable=day,bd=5,fg="blue",font=("Helvetica",12))
da.place(x=235,y=340)

d=Label(root,text="activity",bg="brown",font=("Bodoni",12))
d.place(x=150,y=380)
de = Entry(root,textvariable=des,bd=5,fg="blue",font=("Helvetica",12))
de.place(x=235,y=380)

bb1=Button(root, text="Save",bg="red",font=("Helvetica",12), command=savedata)
bb1.place(x=220,y=420)
bb2=Button(root, text="Show",bg="red",font=("Helvetica",12), command=show)
bb2.place(x=280,y=420)

root.mainloop()
