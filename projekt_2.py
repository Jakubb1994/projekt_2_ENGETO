"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Prajzler
email: prajzler25@gmail.com
"""
import random
import time

def generate_secret_number():
    """Generates a random 4-digit number with unique digits, not starting with 0"""
    digits = list(range(1, 10))                  # First digit num. cannot be 0
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    other_digits = random.sample(digits + [0], 3)
    return str(first_digit) + ''.join(map(str, other_digits))

def validate_guess(guess):
    """Validates the user's guess for correct lenght, digits and uniqueness"""
    if len(guess) != 4 or not guess.isdigit():
        return False, "Input must be a 4-digit number."
        if len(set(guess)) != 4:
            return False, "Digits must be unique."
        if guess[0] == '0':
            return False, "Number cannot start with 0."
        return True, ""
        
def evaluate_guess(secret, guess):
    """Evalutes the guess and returns the number of bulls and cows"""
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def save_statistics(attempts, duration):
    """Saves game statistics to a text file and displays stats for the current game."""
    with open("game_statistics.txt", "a") as file:
        file.write(f"Attempts: {attempts}, Time: {round(duration, 2)} seconds\n")
    print("Statistics for this game:")
    print(f"- Total attempts: {attempts}")
    print(f"- Total time: {int(duration // 60)} minutes and {int(duration % 60)} seconds")

def display_separator():
    """Display a visual separator."""
    print("=" * 50)

def view_statistics():
    """Displays all saved statistics from the game_statistics.txt file."""
    try:
        with open("game_statistics.txt", "r") as file:
            print("\n=== Game Statistics ===")
            for line in file:
                print(line.strip())
            print("=======================\n")
    except FileNotFoundError:
        print("No statistics available. Play a game first!\n")

def play_game():
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ")
        display_separator()
        is_valid, message = validate_guess(guess)

        if not is_valid:
            print(message)
            display_separator()
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        display_separator()

        if bulls == 4:
            end_time = time.time()
            duration = end_time - start_time
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"It took you {round(duration, 2)} seconds.")
            print(f"Total time: {int(duration // 60)} minutes and {int(duration % 60)} seconds.")
            print("That's amazing!")
            display_separator()

            save_statistics(attempts, duration)
            print("Game statistics have been saved.")
            break

if __name__ == "__main__":
    while True:
        print("1. Play game")
        print("2. View statistics")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            play_game()
        elif choice == "2":
            view_statistics()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
