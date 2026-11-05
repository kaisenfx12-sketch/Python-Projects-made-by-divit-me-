#---------------------- Parameter functions--------------------
#User defined functions has two types of functions.
#1. Non parameter function : We do not pass anything in () is called as non parameter function.

def number():
    #code
    pass


number()


#2. parameter Function : These are thsoe function in whcih we pass variables in ().
#eg : we have code and we need to use it again but whenever we want to use it with differet value
#so we get different answer.

#syntax to craete function : 
#def functioname(variable):
#  code


#syntax to call the function :
#functioname(value)


#craete a paraeter function  number . check if no is divsisble by 8, the print no is divisisble by 8, else print it is not divisble by 8.

def number1(no):
    if no%8==0:
        print("it is divisisble by 8")
    else:
        print("it is not divisible by 8")


number1(100) # no variabke is replaced with number here when we call it
number1(200)
number1(800)

#everytime we call teh function w ecan change the value and we get difefernt answer. 
#------------Advantage----------
#1. when whole code is smae only 1/ 2 value is differenr then in place of value use variable 
#when we call the pass we give actual value
#2. this saves time and makes code shorter.

#2. craete a function name paramter function. hekc if variable is red, the print stop else print go

def trafficlight(name):
    if name == "red":
        print("stop")
    elif name == "yellow":
        print("move slowly")
    else:
        print("go")
        



trafficlight("red")
trafficlight("yellow")
trafficlight("green")
    
    
