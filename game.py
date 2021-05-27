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


if (user_choice == computer_choice):
    print("Tie Game:")
elif(computer_choice=="Rock"):
    if(user_choice=="Scissors"):
        print("Rock beats scissors. Computer Wins!")
    else:
        print("Paper beats Rock. Congrats, you win!")
elif(computer_choice=="Scissors"):
    if(user_choice=="Rock"):
        print("Rock beats scissors. You Win!")
    else:
        print("Paper Loses to Scissors. Computer Wins!") 
elif(computer_choice=="Paper"):
    if(user_choice=="Rock"):
        print("Paper Covers Rock. Computer Wins!")
    else:
        print("Paper Loses to Scissors. You Win!")  
print("END OF GAME, THANKS FOR PLAYING")
