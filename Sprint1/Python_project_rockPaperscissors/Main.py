import random

rounds_played=0
user_wins=0
computer_wins=0
draws=0

print("Welcome to the Rock ,paper and Scissors Game!")
print("Rules:")
print("Rock beats Scissors (Rock crushes Scissors)")
print("Scissors beats Paper (Scissors cut Paper)")
print("Paper beats Rock (Paper covers Rock)")

while True:
##User Choice
    user_choice=input("Enter your choice (rock,paper or scissors) or 'q' to quit : ")

    if user_choice.lower()=="q":
        break
    print("Your choice:",user_choice)
    
    if user_choice!="rock" and user_choice!="paper" and user_choice!="scissors":
        print("\nPlease choose only rock, paper or scissors\n")
        break
    
    choices=["rock","paper","scissors"]
    computer_choice=random.choice(choices)

    if user_choice==computer_choice:
        result="Draw"
        draws+=1
    elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="scissors" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock"):
        result="Win"
        user_wins+=1
    else:
        result="Lose" 
        computer_wins+=1       
     
    rounds_played+=1   
    print(f"Computer Choice:{computer_choice}")
    print(f"Result:{result}")  
    print("Rounds played:", rounds_played)
    print("User wins:", user_wins)
    print("Computer wins:", computer_wins)
    print("Draws:", draws)  