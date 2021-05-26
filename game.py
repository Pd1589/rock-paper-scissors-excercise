# game.py
import random
print("Rock, Paper, Scissors, Shoot!")
user_choice = input("Please choose one of: 'Rock' ,'Paper' ,'Scissors' --->")
print("USER CHOICE: ", user_choice)
#EXIT IF INVALID ENTRY 
if (user_choice == "Rock") or (user_choice == "Paper")or (user_choice == "Scissors"):
    print("VALID ENTRY KEEP GOING")
else:
    print("Invalid Entry, Please Try Program Again")
    exit()

valid_options = ["Rock","Paper","Scissors"]   
computer_choice= random.choice(valid_options)
print("Computer Choice:",computer_choice)
print("END OF GAME, THANKS FOR PLAYING")
