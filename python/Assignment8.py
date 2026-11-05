"""

1. Write a program that asks the user for a number and checks whether it is positive, negative, or zero.
2. Write a program that asks the user for their age. If the age is 18 or above, print "You can vote", otherwise print "You cannot vote".
3. Write a while loop to print numbers from 1 to 20.
4. Write a while loop to print all even numbers from 2 to 20.
5. Ask the user to enter a number. Keep asking until they enter a number greater than 10.
6. Create a program that keeps asking the user to enter a password. If the password is "python", print "Correct Password" and stop the loop.
7. Create an infinite while True loop that continuously asks:
1 → Print "Hello"
2 → Print "Welcome"
3 → Stop the program using break
Any other number → Print "Invalid choice"
8. Write a program that asks the user for numbers repeatedly and keeps adding them. Stop when the user enters 0, then print the total.

9. Write a program that keeps asking for marks. For every mark:

90+ → "A"
75–89 → "B"
50–74 → "C"
Below 50 → "Fail"

Stop when the user enters -1.

10. Create a simple guessing game using while True. Keep asking the user to guess a secret number. Print "Too high", "Too low", or "Correct!". Stop when the answer is correct.


"""


#1

a=int(input("Enter Number"))
if a== -1:
    print("negative")
elif a== +1:
    print("positive")
elif a==0:
    print("zero")

#2

age=int(input("Enter Age"))
if a < 18:
    print("you cannot vote")
else:
    print("You cannot vote")

# 3
number = 1
while number <= 20:
    print(number)
    number += 1

# 4
number = 2
while number <= 20:
    print(number)
    number += 2

# 5
number = int(input("Enter a number greater than 10: "))
while number <= 10:
    number = int(input("Try again: "))
print("ok")

# 6
while True:
    password = input("Enter password: ")
    if password == "python":
        print("Correct Password")
        break

# 7
while True:
    choice = input("1: Hello, 2: Welcome, 3: Stop: ")
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Welcome")
    elif choice == "3":
        break
    else:
        print("Invalid choice")

# 8
total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total += number
print("Total:", total)

# 9
while True:
    marks = int(input("Enter marks (-1 to stop): "))
    if marks == -1:
        break
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 50:
        print("C")
    else:
        print("Fail")

# 10
secret_number = 7
while True:
    guess = int(input("Guess the secret number: "))
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break

        
