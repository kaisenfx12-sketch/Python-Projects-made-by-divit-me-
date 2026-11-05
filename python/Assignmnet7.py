#------Assignmnet-----------
#reate an infinite loop that asks the user to enter a number.
"""
1. If the user enters 0, stop the loop using break.
    Otherwise, print the number.
Keep asking until the user enters 0.

2. Skip Even Numbers

Use a while loop from 1 to 20.

Use continue to skip even numbers.
Print only the odd numbers.


3. Skip and Stop

Write a program that runs from 1 to 20.

If the number is 5, use continue.
If the number is 15, use break.
Print all other numbers.

"""
#assignment
#|
#V

#1

while True:
    ask = int(input("Enter Number: "))
    if ask == 0:
        break
    else:
        print(ask)
        continue

# 2. Skip even numbers
 

a=1
while a<=20:
    if a%2==0:
      continue
    a+=1
    print(a)
     

     
# 3. Skip 5 and stop at 15

a=1
while a<=20:
    if a==5 :
      continue
    if a==15:
        break
    a +=1
    print(a)



    


    

