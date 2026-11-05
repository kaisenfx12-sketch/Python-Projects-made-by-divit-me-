"""
Create a tuple of 5 numbers and use len() to find the number of elements.
Create a tuple of numbers and use max() and min() to find the largest and smallest values.
Create a tuple of numbers and use sum() to calculate the total.
Create a tuple with repeated values and use count() to find how many times a particular value appears.
Create a tuple of fruits and use index() to find the position of "mango".
Create a tuple of numbers and use sorted() to display the numbers in ascending order.
Create a tuple of numbers and use sorted() to display the numbers in descending order.

"""

#1

tp12=(14,78,23,28,34)
print(tp12)
print(tp12[2])

print(len(tp12))


#2

tp13=(21,18,16,9)
print(tp13)
print(tp13[2])

print(min(tp13))
print(max(tp13))


#3

tp14=(34,89,23,45)
print(tp14)
print(tp14[2])

print(sum(tp14))

#4

tp1 = (34, 89, 34, 23, 34)
print(tp1.count(34))

#5

tp15=("mango","apple","banana")
print(tp15)
print(tp15[2])

if "mango" in tp15 :
    print("its there")
else:
    print("its not there")





#6

tp16=(1534444346457754545457557745,200000000,309,421,575839753835892)
print(sorted(tp16))



#7

print(sorted(tp16,reverse=True))











