import random

def get_user_choice():
    """
    Prompt the user to enter their choice and validate the input.
    Returns the user's choice if valid.
    """
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    print("\nChoose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choice = input("Enter the number of your choice (1-3): ")
    if choice in choices:
        return choices[choice]
    else:
        print("Invalid choice. Please select a number between 1 and 3.")
        return None

def get_computer_choice():
    """
    Generate a random choice for the computer.
    Returns the computer's choice as a string.
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user's and computer's choices.
    Returns 'user', 'computer', or 'tie' based on the result.
    """
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    """
    Display the result of the round, including choices and the winner.
    """
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    print("Welcome to the Rock-Paper-Scissors Game!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            continue
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nScores:\nYou: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
