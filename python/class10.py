#---------------Tuple and Dictonary ---------------------

# Tuple are used to store data   like  list it can store lot of data but once eh dta is stire cannot be cahnged. 
#it is fixed. immutable. cannot be chamged. infinite data can be stored. () is used .

#syntax to craete tuple : tup;lename=(value1, va;ue2...)


#-----------Index value for tuple--------------
#Index value menas position number given to everu data  in tuple which starts from 0, 1, 2...

tp11=(12, 78, 90, "hello")
print(tp11)
print(tp11[2])

#---------Function in tuple-------------
#1. count() : counts how many times.  value come in  tuple 

tp1=tp11.count(78)
print(tp1)


#2. len() : gives current size of tuple.  this function is also there in list.

print(len(tp11))

#3. min(), max(), sum() : minimum number, m aximum number and s um is to add all numbers . 

tpp=(12, 67, 67, 45, 23) 

print(min(tpp))
print(max(tpp))
print(sum(tpp))

#4. in means ti chekc if value exist in tuple ir not  

if  23 in tpp :
    print("its not there") 
else:
    print("its tehre ") 

#5. sorted() : sorts data tuple 
print(sorted(tpp))
print(sorted(tpp, reverse=True))
  



















