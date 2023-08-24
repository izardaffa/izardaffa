import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    rock_win = "Rock smashes scissors!"
    paper_win = "Paper covers rock!"
    scissors_win = "Scissors cut paper!"

    win = "You win!"
    lose = "You lose."

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return f"{rock_win} {win}"
        else:
            return f"{paper_win} {lose}"
    elif player == "paper":
        if computer == "rock":
            return f"{paper_win} {win}"
        else:
            return f"{scissors_win} {lose}"
    elif player == "scissors":
        if computer == "paper":
            return f"{scissors_win} {win}"
        else:
            return f"{rock_win} {lose}"
    else:
        return "Invalid. Chose between rock, paper, and scissors"
    
choice = get_choices()
result = check_win(choice["player"], choice["computer"])

print(result)