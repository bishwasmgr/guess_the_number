import random

class GuessTheNumberGame:
    def __init__(self):
        self.secret_number = self.generate_random_number()
        self.attempts = 0

    def generate_random_number(self):
        return str(random.randint(1000, 9999))

    def get_feedback(self, guess):
        feedback = ""
        for i in range(4):
            if guess[i] == self.secret_number[i]:
                feedback += "o"
            elif guess[i] in self.secret_number:
                feedback += "x"
            else:
                feedback += "-"
        return feedback

    def play_game(self):
        print("Welcome to Guess the Number Game!")
        print("Try to guess the 4-digit secret number.")
        
        while True:
            guess = input("Enter your guess (4-digit number) or 'q' to quit: ")
            
            if guess.lower() == 'q':
                print(f"The secret number was {self.secret_number}.")
                print("Thanks for playing!")
                break
            
            if not guess.isdigit() or len(guess) != 4:
                print("Invalid input. Please enter a 4-digit number.")
                continue
            
            self.attempts += 1
            feedback = self.get_feedback(guess)
            
            if feedback == "oooo":
                print(f"Congratulations! You've guessed the number {self.secret_number} in {self.attempts} attempts.")
                break
            else:
                print("Hints:", feedback)

if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.play_game()
