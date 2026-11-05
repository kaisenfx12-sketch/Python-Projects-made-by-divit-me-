#------------------------Functions-------------
#Functions means to do som.e work. There are two tyoe of functions :
#1. Inbuilt Functions : These are those functons which are already there inside the python and we are just using them.
#eg : input(), print(), sort(), reversee()...
#Functions ahve one word,  and they do something for us. and they ahve ()
#along them.

#2. User defined function : These are those functions whcih are created by user.  and later we use them.
#creating the function means we are actually grouping the code together. 
#storing the code is creating ouw function.. we can store anything in function if else, for loop whike loop, list, variables...
#anything as much as we can store
#same as variables whcih store one value 
#list/tuple/dictonary  whch stores values.
#Reason for creating our own function :
#1. We are storing the code so that we can use it again...
#We can use it again by calling functions or write the function name 
#without storing the code we have to copy paste
#2. coe becomes organized
#3. if looking for a function but there is a no  inbuilt function  then in that case we craete our own function.

#Best benefit is we can / use as many times we can.

#eg : if ether is code whcih  need to sue at different places then ony way is copy and paste.
#loop repeats one after te other. so functions is the only way to use code at difefrent pkaces
#copy and paste incraese the space.
#syntax to craete our own function :
#def functioname():
#  code


#syntax to call function :
#functioname()



#----------------------------------------------
#crate a function and insude that use input to take number  and use if else itochekc whether no is greater thah 18 
#then print adult else print kid.

def number():
    no=int(input("Enter number : "))
    if no >18 :
        print("adult")
    else:
        print("kid")

#1 times if we call the function then one time code will work 
number()
number()
#no if times we call function that many times code will work 