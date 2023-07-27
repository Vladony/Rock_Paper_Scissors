import random

computer_score = 0
player_score = 0
choices = ["rock", "paper", "scissors"]
while True:
    number = input("Please select winning number of games: ")
    if not number.isdigit():
        print("please enter a valid whole number.")
        continue
    else:
        number = int(number)
        break

while max(player_score, computer_score) < number:
    computer_guess = random.choice(choices)
    player_guess = input("Please enter your guess: ")

    if player_guess not in choices:
        print("Please select one of the following: 'rock', 'paper', 'scissors'")
        continue

    #all equal
    if computer_guess == player_guess:
        print("Draw! Try again!")

    #player_win
    elif player_guess == "rock" and computer_guess == "scissors":
        print("rock beats scissors! You win!")
        player_score += 1

    elif player_guess == "paper" and computer_guess == "rock":
        print("paper beats rock! You win!")
        player_score += 1

    elif player_guess == "scissors" and computer_guess == "paper":
        print("scissors beat paper! You win!")
        player_score += 1

    #computer_wins
    else:
        print(f"Sorry {computer_guess} beats {player_guess}! You lose!")
        computer_score += 1

    print(f"Player score: {player_score}\nComputer score: {computer_score}")

print(f"Game has ended. Computer score: {computer_score}, Player score: {player_score}.")