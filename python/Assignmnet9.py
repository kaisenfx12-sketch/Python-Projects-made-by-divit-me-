"""

Create a list of 8 numbers. Print the first, third, and last elements using their index values.
Create a list of 6 fruits. Ask the user for a fruit and use index() to find its position.
Create a list of numbers. Add a new number at index 2 using insert() and print the list.
Create a list of names. Remove the element at index 3 using pop() and print the removed name.
Create a list of numbers. Find the index of the largest number without using max().
Create a list of 10 numbers. Print all elements from index 2 to index 6 using slicing.
Create a list of numbers with repeated values. Ask the user for a number and use count() to find how many times it appears.
Create a list of numbers. Add two new numbers using append(), then sort the list in descending order.
Create a list of student names. Ask the user for a name. If it exists, print its index position; otherwise print "Name not found"

"""


# 1. Print selected elements from a list.
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[0], numbers[2], numbers[-1])

# 2. Find the position of a fruit.
fruits = ["apple", "banana", "orange", "mango", "grape", "pear"]
fruit = input("Enter a fruit: ")
if fruit in fruits:
	print(fruits.index(fruit))
else:
	print("Fruit not found")

# 3. Insert a number at index 2.
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)
print(numbers)

# 4. Remove and print the element at index 3.
names = ["Aarav", "Diya", "Kabir", "Meera", "Riya"]
print(names.pop(3))

# 5. Find the index of the largest number without using max().
numbers = [12, 45, 7, 89, 34, 23]
largest_index = 0
for index in range(1, len(numbers)):
	if numbers[index] > numbers[largest_index]:
		largest_index = index
print(largest_index)

# 6. Print elements from index 2 through index 6.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[2:7])

# 7. Count how many times a number appears.
numbers = [2, 4, 2, 6, 8, 2, 10, 4]
number = int(input("Enter a number: "))
print(numbers.count(number))

# 8. Append two numbers and sort in descending order.
numbers = [5, 1, 9, 3]
numbers.append(7)
numbers.append(2)
numbers.sort(reverse=True)
print(numbers)

# 9. Find a student's index position.
students = ["Aarav", "Diva", "Kabir", "Meera", "Riya"]
student = input("Enter a student name: ")
if student in students:
	print(students.index(student))
else:
	print("Name not found")                                         

