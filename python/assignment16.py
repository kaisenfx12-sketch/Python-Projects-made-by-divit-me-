#Adventure Game, Loops, Functions, Lists, and Tuples Question 1: Treasure Adventure Game Create an adventure game using input(), if-elif-else, and a while loop. - Ask the player to enter their name. - Give the player three choices: enter a forest, explore a cave, or cross a river. - Each location should have a different result. - If the player finds the treasure, display a winning message. Allow the player to continue playing until they choose to quit.

#Adventure Game, Loops, Functions, Lists, and Tuples Question
#  1: Treasure Adventure Game Create an adventure game using
#  input(), if-elif-else, and a while loop. - 
#Ask the player 
# to enter their name. - Give the player three choices: 
# enter a forest, explore a cave, or cross a river. - Each 
# location should have a different result. - If the player 
# finds the treasure, display a winning message. - Allow the
#  player to continue playing until they choose to quit


name=input("enter name : ")
print("Welcome ! !!", name)

choice=input("Enter teh location you wnat to go forest, cave, river : ")
if choice=="forest":
    print("Let go to forest..")
    print("There is a house in forest....")
    forest=input("enter the choice if you want to go in house : ")
    if forest=="house":
       print("you enter the house...")
       print("a witch found you and poisened you and you died")
       print("you lose!!",name)
    else:
        print("you are safe")


if choice=="cave":
    print("Lets go to the cave")
    print('you see a sage meditating in the cave')
    cave=input("enter if you want to go near sage : ")
    if cave=="yes":
        print("you go near the sage and start meditating with him and leart the art of the mind")
    else:
        print("you dont go near the sage and else fall and get embarresed")
        print("you lose!!",name)

if choice=="river":
    print("lets go cross the river")
    print("you see a man and treasure at the end of the bridge on which u are crossing the river on")
    river=input("enter if you want to cross river or you dont : ")
    if river=="yes":
        print("you cross the river but the man has a poisonous needle but you take the poisonous needle from him and poke him with it and take the treasure and run")
        print("you win!!,",name)
    else:
        print("you dont cross the ruver and the man lunges at you and pokes you with the needle and you die.")
        print("you lose!!",name)



    #adventure game done wallaaaa feast your eyes fro the most amazing game THE ADVENTURE GAME!!!
