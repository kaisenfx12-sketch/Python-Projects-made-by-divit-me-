#----------------for loop------------------------
#for loop is used to loop over the data, we use always the for loop herever there is data  lie list, tuple, dictonary.
#why it is used on them 

#eg : we have. if else condition whcih we need to use on all values in list, tuple, dictonary.
#There is a list of numbers. we need to use if else to chekc whcih one is even number and which one is odd number.
#We ahve to use if else multiple ti mes on all values in list. if there are 10 numbers in list  we have to use 
#if 10 times.

#Method2 :  we use for loop, and we tell for loop to use if else on all values. 
#So if tehre is a code we need to use repeatedly on all values we can use for loop it will use on it.

#syntax:
#for variablename in list/tuple/dictonaryname:

#--------------------------------difference betwween while loop or for loop----------------------
#1. whie loop is used to reoeta the code no of times we mention or till the time condition is true.
#but for loop is mostly used on list, tuple, dictonary.  to repeat code n the valus. for loop repeats 
#as according to the values given. if there are 5  value it will repeat 5 times.


#-----------------------------------------------

list1=[12, 89, 77, 90, 100]

for i in list1: # i goes inside list1 , uses  code given  one by one on all values in list
   if i%2 ==0: # i goes  and brings value. firts i=12, then i=890, them so on..
      print(i, "is even ")
   else:
	   print(i, "is odd")
       
list2=["apple", "banana"]

for i1 in list2:
   print(i1) # i1 will gte all values from list2 and print them 


#same for tuples

   
#-------------------for loop dictonary---------------------------
#dictonary has keys and values both so we have to create two variables. and use the function items()


# a dictionary containing a student's subjects and marks:

marks = {
    "English": 85,
    "Maths": 90,
    "Science": 78,
    "Computer": 95,
    "Hindi": 88
}

#Using a for loop:

#Print each subject and its marks.
#Calculate the total marks.
#Calculate the percentage.


#----------when we need both  keys and values--------
t=0
for i, x in marks.items():
   #i is to get keys : subject
   #x  is for values
   print(i , ":", x)
   t +=x # x will get values(marks)
   # keep on ading and storing in t
print('Total ', t)
percent= (t*100)/500
#total  for lal subjects : 500
print('Percent', percent)

#-----whne need only keyes---------

for i1 in marks.keys():
   print(i1)


#when need only values----------

for i11 in marks.values():
   print(i11)








