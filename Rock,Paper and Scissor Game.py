import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play a game of Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")

    # Get the user's choice
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()

    # Get the computer's choice
    computer_choice = get_computer_choice()

    # Display the choices
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Start the game
if __name__ == "__main__":
    play_game()
