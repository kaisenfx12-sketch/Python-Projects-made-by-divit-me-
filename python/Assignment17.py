"""

Part 1: Create the player
1. Create a dictionary called player.
2. Store the player's name, score, and lives in it.
3. Ask the player to enter their name using input().
4. Display a welcome message using their name.
5. Set the initial score to 0 and lives to 3.




Part 2: Create the quiz
6. Create a tuple containing five quiz questions.
7. Create a second tuple containing the five correct answers in the same order.
8. Use a for loop to ask each question.
9. Take the player's answer using input().
10. Use an if-else condition to check whether the answer is correct.




Part 3: Collect coins and rewards
11. Give the player 10 points for each correct answer.
12. If the answer is incorrect, reduce the player's lives by one.
13. Create an empty list called rewards.
14. Add "Gold Coin" to the list whenever the player answers correctly.
15. If the player answers three questions correctly, add "Magic Key" to the rewards list.




Part 4: Add game conditions
16. If the player's lives reach zero, display "Game Over!".
17. Use a while loop to keep the game running while the player has lives remaining and questions are available.
18. If the score is 50, display "Coding Champion!".
19. If the score is between 20 and 40, display "Great Job, Explorer!".
20. Otherwise, display "Keep Practising!".




Part 5: Use functions
21. Create a function called start_game() to welcome the player.
22. Create a function called play_game() to run the quiz.
23. Create a function called show_result() to display the final score, lives, and rewards.
24. Call all three functions in the correct order.
25. At the end, display the player's name, total score, remaining lives, and collected rewards.

"""

player_info = {
    'name': "Divit",
    'score': 0,
    'lives': 3
    
}

name=input("Enter Name")
print("Welcome to the quiz game!",name)
score=0
lives=3

tp2=(1. 10*10 2.:20/5 3.: 2*20 4:5*10 5:6*20 )
answer1=input("Enter Answers of 1st question")
if answer1 == "100":
    print("Correct!")
else:
    print("Incorrect!")