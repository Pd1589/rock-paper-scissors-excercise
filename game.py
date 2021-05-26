# game.py

print("Rock, Paper, Scissors, Shoot!")
user_choice = input("Please choose one of: 'Rock' ,'Paper' ,'Scissors' --->")
print("USER CHOICE: ", user_choice)
#EXIT IF INVALID ENTRY 
if (user_choice == "Rock") or (user_choice == "Paper")or (user_choice == "Scissors"):
    print("VALID ENTRY KEEP GOING")
else:
    print("Invalid Entry, Please Try Program Again")
    exit()
    


print("END OF GAME, THANKS FOR PLAYING")