import random

def generate_random_number():
    return ''.join(random.sample('0123456789', 4))

def compare_numbers(secret_number, guess):
    result = ""
    for i in range(4):
        if guess[i] == secret_number[i]:
            result += "O"
        elif guess[i] in secret_number:
            result += "X"
    return result

def play_game():
    secret_number = generate_random_number()
    attempts = 0

    while True:
        guess = input("Enter your guess (4-digit number) or 'q' to quit: ")
        
        if guess.lower() == 'q':
            print("Quitting the game.")
            break
        
        if not guess.isdigit() or len(guess) != 4:
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        attempts += 1
        result = compare_numbers(secret_number, guess)
        
        if result == "OOOO":
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        else:
            print("Hints:", result)

if __name__ == '__main__':
    play_game()
