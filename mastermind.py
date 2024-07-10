import random


def get_hint(secret, guess):
    correct_digits = sum(s == g for s, g in zip(secret, guess))
    correct_positions = len(set(secret) & set(guess))
    return correct_digits, correct_positions


def play_round(secret):
    attempts = 0
    while True:
        guess = input("Enter your guess: ")
        if guess == secret:
            print("Correct! You've guessed the number.")
            return attempts + 1
        attempts += 1
        correct_digits, correct_positions = get_hint(secret, guess)
        print(f"Correct digits in the correct position: {correct_digits}")
        print(f"Correct digits but in the wrong position: {correct_positions}")


def play_game():
    print("Welcome to Mastermind!")

    # Player 1 sets the number
    player1_secret = input("Player 1, set the number: ")
    print("\n" * 50)  # Clear the screen
    print("Player 2, it's your turn to guess the number.")
    player1_attempts = play_round(player1_secret)
    print(f"Player 2 guessed the number in {player1_attempts} attempts.")

    # Player 2 sets the number
    player2_secret = input("Player 2, set the number: ")
    print("\n" * 50)  # Clear the screen
    print("Player 1, it's your turn to guess the number.")
    player2_attempts = play_round(player2_secret)
    print(f"Player 1 guessed the number in {player2_attempts} attempts.")

    # Determine the winner
    if player1_attempts < player2_attempts:
        print("Player 1 wins the game and is crowned Mastermind!")
    elif player1_attempts > player2_attempts:
        print("Player 2 wins the game and is crowned Mastermind!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()
