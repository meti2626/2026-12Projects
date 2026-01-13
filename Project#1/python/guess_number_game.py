import random

def play_game():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get player input
            user_input = input("Enter your guess (or 'q' to quit): ")
            
            if user_input.lower() == 'q':
                print(f"The number was {secret_number}. Thanks for playing!")
                break
            
            guess = int(user_input)
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                
                # Ask to play again
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower().startswith('y'):
                    secret_number = random.randint(1, 100)
                    attempts = 0
                    print("\nI'm thinking of a new number between 1 and 100.")
                else:
                    print("Thanks for playing!")
                    break
                    
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()
