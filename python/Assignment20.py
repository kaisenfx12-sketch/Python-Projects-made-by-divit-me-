from tkinter import *
s=Tk()
s.title("BMI calculator app")
s.geometry("600x600")
 

l1=Label(s, text="Enter your name:")
l1.grid(column=0, row=0)

e1=Entry(s)
e1.grid(column=1, row=0)

l2=Label(s, text="Enter your weight(kg):")
l2.grid(column=2, row=0)

e2=Entry(s)
e2.grid(column=3, row=0)

l3=Label(s, text="Enter your height(cm):")
l3.grid(column=4, row=0)

e3=Entry(s)
e3.grid(column=5, row=0)

b1=Button(s, text="Calculate BMI", width=10, height=2, bg="green", fg="white", font=("New Times Roman", 20))
b1.grid(column=9, row=5)

mainloop()