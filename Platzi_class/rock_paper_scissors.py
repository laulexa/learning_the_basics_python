player_1_choice = input("Enter rock paper or scissors: ").lower()
player_2_choice = input("Enter rock paper or scissors: ").lower()

print("player_1_choice: ", player_1_choice)
print("player_2_choice: ", player_2_choice)

valid_choices = ["rock", "paper", "scissors"]

if player_1_choice not in valid_choices:
    print("that's not an option player 1, try again")
elif player_2_choice not in valid_choices:
    print("that's not an option player 2, try again")
elif player_1_choice == player_2_choice:
    print("try again")
elif (
    (player_1_choice == "rock" and player_2_choice == "scissors") or 
    (player_1_choice == "paper" and player_2_choice == "rock") or 
    (player_1_choice == "scissors" and player_2_choice == "paper")
    ):
    print("player One wins")
else:
    print("Player Two wins")