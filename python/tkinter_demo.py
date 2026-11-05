from tkinter import*

divit=Tk()
divit.title("A Demonstration")
divit.geometry("650x650")

li=Label(divit, text="you like it?")
li.grid(row=0, column=0)

b1=Button(divit, text="Sumbit")
b1.grid(row=0, column=1)

e1=Entry(divit)
e1.grid(row=1, column=0)

mainloop()
