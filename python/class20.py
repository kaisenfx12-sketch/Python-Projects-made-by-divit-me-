#------------------to get value from entry------------
#1. get() : get() is used to get the value from entrybox
#---to get text value
#syntax : variable=entrybox.get()

#value will be stored 

#---to get int value ------
#syntax : variable=int(entrybox.get())

#------------after cakculating answer ti show answer--------
#to show answer inside entrybox 

#1. craete tkinter variable 
#syntax : variablename=StringVar()
#set() use this to put answer in  tkinter variable 
#variable.set(answer)
#from tkinter varaible anwer goes to entrybox


#-------to show answrr with label--------
#1. craete a label : l1=label()
#2. l1.config(answer)



#Note : do all code i function  and cll function on button 
#command=functioname


from tkinter import *
s=Tk()
s.title("login page")
s.geometry("600x600")

l1=Label(s, text="E-Mail")
l1.grid(row=0, column=0)

e1=Entry(s)
e1.grid(row=1, column=0)

l2=Label(s, text="Password")
l2.grid(row=3, column=0)

e2=Entry(s, text="*")
e2.grid(row=4, column=0)

def login():
    #gte values fro entry
    #email="divit@gmail.com", password=122345
    if e1.get() == "divit@gmail.com" and e2.get()=="12345":
        l3.config(text="Email and password is correct")
    else:
        l3.config(text="email and password is wrong")



l3=Label(s)
l3.grid(row=7, column=0)
b1=Button(s,text="Sumbit", width=10, height=2, bg="blue", fg='white', font=("New Times Roman", 10), command=login)
b1.grid(row=6, column=0)











mainloop()

#Assignmnet 
#create BMI APP
#weight/height

