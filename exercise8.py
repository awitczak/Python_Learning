print("Welcome to rock, paper, scissors!\n\n\n")

choice = "yes"

while choice == "yes" :
    player_1 = input("Player 1 chooses: ")
    player_2 = input("Player 2 chooses: ")
    if player_1 == player_2:
        continue
    elif player_1 == "paper" and player_2 == "scissors":
        choice = input("Player 2 wins! Do you want to play again? Entry (yes/no): ")
    elif player_1 == "paper" and player_2 == "rock":
        choice = input("Player 1 wins! Do you want to play again? Entry (yes/no): ")
    elif player_1 == "rock" and player_2 == "paper":
        choice = input("Player 2 wins! Do you want to play again? Entry (yes/no): ")
    elif player_1 == "rock" and player_2 == "scissors":
        choice = input("Player 1 wins! Do you want to play again? Entry (yes/no): ")
    elif player_1 == "scissors" and player_2 == "paper":
        choice = input("Player 1 wins! Do you want to play again? Entry (yes/no): ")
    elif player_1 == "scissors" and player_2 == "rock":
        choice = input("Player 2 wins! Do you want to play again? Entry (yes/no): ")