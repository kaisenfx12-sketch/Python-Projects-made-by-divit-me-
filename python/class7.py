#-------------------while True----------------------------------
#while is also used to create infinite loop. 
#we use True keyword to create a infinite loop. 
#True means yes when we place in condition that stops the loop. infinite loop is created

#--------only two things we give--------
#1. True 
#2. code to repeat


#syntax:
#while True :
#   code


#print hi repeatedly on screen 


#while True:
    #print("hi")


#while True:
#   print(2)


#--------------------break and continue keyowrds----------------
#break is used to stops the loop infinite loop completely by giving the condition. 
#continue restarts the loop again at aby given condition


#1. take password from user. id password is sorrec then break the loop else contiue asking password till time correct password given 


while True:
    ask=input("Enter the password : ")
    if ask=="12345":
        print("correct")
        break
    else:
        print("incorrect")
        continue 


#infinite loop is used whe wedo not know at what number needs to be stopped, we only know condition. create a infinite loop
