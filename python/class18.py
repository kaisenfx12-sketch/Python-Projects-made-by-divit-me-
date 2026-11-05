#----------------tkinter Library -------------------
#tkinter library is used to create an interface. It is used to develop. 
#GUI(graphical user interface.). It ismused to craete software/desktops.
#small softwwares eg : notepad, Billing softwares, calculator, librray/student software, 
#employee sosftwares, quiz software, To do list app..

#tkinter widgets :  creates buttons, labels, textboxes, checkbox, entrynoxes..
#These are called as tkinter widgets

#----Basic Structure ----
#1. import tkinter library.
#2. create a a screen : Tk(). 
#screename=Tk()
#screeame is variablw wich ca be anything 
#3. create a title
#screename.title("")
#4. craete a screen size
#screename.geonetry("widthxheight")
#5. at teh end always use mainloop()
#mainloop() is infinite loop we use at the end so that it runs everything we created above.
#* means all everything is imported


#-------------------Two ways tos et position----------------
#1. grid(row=0, column=0) : we set in rows and columns
#2. place(x=, y=) : 
from tkinter import *


s=Tk()
s.title("My first app")
s.geometry("600x600")

#label
#syntax : variablename=Label(screen, text=" ")
l1=Label(s, text="hello")
l1.grid(row=0, column=0)

#button
b1=Button(s, text="Submit")
b1.grid(row=0, column=1)

#entry: textbox
e1=Entry(s)
e1.grid(row=1, column=0)



mainloop()






