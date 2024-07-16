import random

def provide_feedback(secret, guess):
    correct_position = 0
    correct_digit = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            correct_position += 1
        elif guess[i] in secret:
            correct_digit += 1
    return correct_position, correct_digit

def play_round(secret_number, player_name):
    attempts = 0
    while True:
        guess = input(f"{player_name}, enter your guess: ")
        attempts += 1
        correct_position, correct_digit = provide_feedback(secret_number, guess)
        if correct_position == len(secret_number):
            print(f"Correct! {player_name} guessed the number in {attempts} attempts.")
            break
        else:
            print(f"Feedback: {correct_position} digits in the correct position, {correct_digit} correct digits in the wrong position.")
    return attempts

def determine_winner(player1_choice, player2_choice):
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif rules[player1_choice] == player2_choice:
        return "Player 1 wins and is crowned Mastermind!"
    else:
        return "Player 2 wins and is crowned Mastermind!"

def main():
    num_digits = int(input("Enter the number of digits for the secret number: "))

    # Player 1 sets the number
    player1_number = input("Player 1, enter the number for Player 2 to guess: ")

    # Player 2 guesses Player 1's number
    print("Player 2's turn to guess.")
    player2_attempts = play_round(player1_number, "Player 2")

    # Player 2 sets the number
    player2_number = input("Player 2, enter the number for Player 1 to guess: ")

    # Player 1 guesses Player 2's number
    print("Player 1's turn to guess.")
    player1_attempts = play_round(player2_number, "Player 1")

    # Determine the winner based on Rock-Paper-Scissors rules
    player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
    player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

    result = determine_winner(player1_choice, player2_choice)
    print(result)

if __name__ == "__main__":
    main()
