#--------------------------Basic Rules in tkinter or syntax----------------------
#------how to0ntet value from textbox 
#get() function is used to get the value.
#syntax : varieblename=textboxname.get()

#-------how to set value or give value to textbox-------
#once answer is calculated we put the result in textbox

#1. first we always create tkinter variable : variablename=StringVar() for textbox
#tkinter are those variables whcih store values from  textbox/ widgets or normal values as well.
#this variable we can connect with widgets : StringVar(), IntVar(), BoolVar() are the variables used to 
#create tkinter variables.  we use function according to what values is being stored.

#syntax : variable=StringVar()
#connect : textvariable=variable

#2. use set on tkinter variable to store result
#s.set(result)

#since tkinter vaiable are connected then from tkinter variable it goes to textbox

#note : this variable is connected to textbox. if we put anuthing in tkinter varaible, automatically goes to textbox, 
#vice vers if put anyting in textbox, it goes to tkinter variable 

#theu bothe are connected

#----------------How to call function tkinter ---------------
#1. paraamter function :  on wbich we have variable in (). when () is not empty
#def functioname(a):

#syntax : command=lambda : functioname(value)


#2. Non paarmeter function : this is taht function in whcih () is empty.
#def functioname():

#syntax : command=functioname

#---------steps to code for press------
#1. craete a   variabke where we store all numbers and signs 
#2. we put a number  for sometimes we will take as a variable. 
#3. we first  put in tkinter variable using set() and from tkinter variable it goes to entrybox


expression=" "
def press(num):# when we call teh function in  place of num the actual number  we will come
    global expression
    expression=expression + str(num)
    #expression has previois number, num is variable which is a new number 
    #tis will join both numbers  and put them in entrbox otehrwise  previous  number is deleted
    #put this in tkinter variable 
    s1.set(expression) # from s1 it goes to e automatically because they are connected


def equal():
    global expression 
    #we can use the inbuilt function eval() : it dioes addition, subtaction, multiplicaton, dividion
    r=eval(expression) # expression  variable has all numbers  and sign 
    # answe is in r variable 
    # from r we put answer in tkinter varaible s1
    s1.set(r)


    


def delete():
    global expression 
    expression= " " # empty 
    s1.set(expression) # pass this to s1 
    


command : press
command : equal
command : delete

#Calculator project in tkinter------------|
from tkinter import*
 

s=Tk()
s.title("Calculator App ")
s.geometry("600x600")


#tkinter variabke 
s1=StringVar() # this variable connect with e

e=Entry(s, width=46, textvariable=s1)# connect s1 with using textvariable 
e.grid(column=0, row=0, columnspan=5, ipady=10)
#we will combine all columns
#bg  = backgroun color, fg=text color, font = font family 

b1=Button(s, text="%", width=3, height=1, bg="white", fg="black", font=("New Times Roman", 20), command=lambda : press("%"))
b1.grid(row=1, column=0)

b2=Button(s, text="+/-", width=3, height=1, bg="white", fg="black", font=("New Times Roman", 20), command=lambda : press("+/-") )
b2.grid(row=1, column=1)

b3=Button(s, text="c", width=3, height=1, bg="white", fg="black", font=("New Times Roman", 20), command=delete )
b3.grid(row=1, column=2)

b4=Button(s, text="AC", width=3, height=1, bg="white", fg="black", font=("New Times Roman", 20), command=delete )
b4.grid(row=1, column=3)

b5=Button(s, text="1",width=3, height=1, bg="white",fg="black", font=("New Times Roman",20), command=lambda : press("1"))
b5.grid(row=2, column=0)

b6=Button(s, text="2", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("2"))
b6.grid(row=2, column=1)

b7=Button(s, text="3", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("3"))
b7.grid(row=2, column=2)

b8=Button(s, text="4", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("4"))
b8.grid(row=2, column=3)

b9=Button(s, text="5", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("5"))
b9.grid(row=3, column=0)

b10=Button(s, text="6", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("6"))
b10.grid(row=3, column=1)

b11=Button(s, text="7", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("7"))
b11.grid(row=3, column=2)

b12=Button(s, text="8", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("8"))
b12.grid(row=3, column=3)

b13=Button(s, text="9", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("9"))
b13.grid(row=4, column=0)

b14=Button(s, text="0", width=3, height=1, bg="white", fg="black",font=("New Times Roman", 20), command=lambda : press("0"))
b14.grid(row=4, column=1)

b15=Button(s, text="=", width=3, height=1, bg="blue", fg="white",font=("New Times Roman", 20), command=equal)
b15.grid(row=4, column=2)

b16=Button(s, text="+", width=3, height=1,  bg="blue", fg="white", font=("New Times Roman", 20), command=lambda : press("+"))
b16.grid(row=1, column=4)

b17=Button(s, text="-", width=3, height=1, bg="blue", fg="white", font=("New Times Roman", 20), command=lambda : press("-"))
b17.grid(row=2, column=4)


b18=Button(s, text="*", width=3, height=1, bg="blue", fg="white", font=("New Times Roman", 20), command=lambda : press("*"))
b18.grid(row=3, column=4)

b19=Button(s, text="/", width=3, height=1, bg="blue", fg="white", font=("New Times Roman", 20), command=lambda : press("/"))
b19.grid(row=4, column=4)

b20=Button(s, text=".", width=3, height=1, bg="blue", fg="white", font=("New Times Roman", 20), command=lambda : press("."))
b20.grid(row=4, column=3)








mainloop()


