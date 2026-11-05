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

b1=Button(s,text="Sumbit", width=10, height=2, bg="blue", fg='white', font=("New Times Roman", 10))
b1.grid(row=6, column=0)
mainloop()

