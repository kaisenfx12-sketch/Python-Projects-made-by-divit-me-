#---------------------List--------------
#List is used to store lot of data. It can store infinite data. [] is used to create a list. 
#syntax 
#listname=[value1, value2...]  value are text, Boolean value, numbers

#----------------Index value-----------------
#Index value means position number given to every data in list. The position number starts from 0, 1,2..
#the index value is there to access specific value in list.

list1=[12, 90, 88, False, 'hi']
print(list1)


#hi
print(list1[4])

#---------------Function of List-------------------
#1. append() : add data in list from end or right side

list1.append("Good")
print(list1)


#2. pop() : deletes data from end or right side 

list1.pop()


print(list1)

#3. count() : count number of times the value is repeating. 

cou=list1.count(12)

print(cou)

#4. sort() : sorts data alphabetically / number in order 

list2=["gii", "hhh", "aaa", "bbb", "ff"]

list2.sort()

print(list2)


list3=[1, 90, 77, 12, 45,78, 67,34, 199, 88]

list3.sort()


print(list3)

#5reverse() : reverse the list 

list3.reverse()

print(list3)

#6 insert() : inserts data at specific index value

list1.insert(3, "code")
print(list1)


#7. remove() : removes spceific item in list

list1.remove('hi')

print(list1)

#8 max() : maximum number 

print(max(list3))

#9. sum(): adds all numbers in list 
print(sum(list3))

#10 min() : minimum number of list
print(min(list3))


#in means to cgeck if value or data exit in list or not. 

list1=[12, 90, 56, 89, "hello"]


if "hello" in list1:
    print("it is there ")
else:
    print("its is not there")
