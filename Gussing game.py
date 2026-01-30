import random
def display_welcome_message():
    print("\n" + "="*60)
    print("        WELCOME TO THE NUMBER GUESSING GAME!")
    print("="*60)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("I'll give you hints along the way!")
    print("="*60 + "\n")


def generate_random_number(min_range=1, max_range=100):
    return random.randint(min_range, max_range)


def get_user_guess():
    while True:
        try:
            guess = input("Enter your guess: ")
            
            guess_number = int(guess)
            
            return guess_number
            
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.\n")


def provide_feedback(guess, target_number, min_range, max_range):
    if guess < min_range or guess > max_range:
        print(f"⚠️  Your guess is outside the valid range ({min_range}-{max_range})!")
        print("Try again with a number within the range.\n")
        return False
    
    if guess == target_number:
        print("🎉 Congratulations! You guessed the correct number!\n")
        return True
    
    difference = abs(guess - target_number)
    
    if guess < target_number:
        print("📉 Too Low!", end=" ")
        
        if difference <= 5:
            print("You're very close! 🔥")
        elif difference <= 10:
            print("Getting warm! 🌡️")
        else:
            print("Try a higher number! ⬆️")
    else:
        print("📈 Too High!", end=" ")
        
        if difference <= 5:
            print("You're very close! 🔥")
        elif difference <= 10:
            print("Getting warm! 🌡️")
        else:
            print("Try a lower number! ⬇️")
    
    print()  
    return False


def display_game_statistics(attempts, target_number):
    print("="*60)
    print("               GAME STATISTICS")
    print("="*60)
    print(f"The number was: {target_number}")
    print(f"Total attempts: {attempts}")
    
    if attempts == 1:
        print("Performance: LEGENDARY! 🏆 First try!")
    elif attempts <= 5:
        print("Performance: EXCELLENT! ⭐⭐⭐")
    elif attempts <= 10:
        print("Performance: GOOD! ⭐⭐")
    elif attempts <= 15:
        print("Performance: FAIR! ⭐")
    else:
        print("Performance: Keep practicing! 💪")
    
    print("="*60 + "\n")


def play_game():
    MIN_RANGE = 1
    MAX_RANGE = 100
    
    display_welcome_message()
    
    target_number = generate_random_number(MIN_RANGE, MAX_RANGE)
    
    attempts = 0
    
    game_won = False
    
    while not game_won:
        attempts += 1
        
        print(f"Attempt #{attempts}")
        
        user_guess = get_user_guess()
        
        game_won = provide_feedback(user_guess, target_number, MIN_RANGE, MAX_RANGE)
    
    display_game_statistics(attempts, target_number)


def ask_play_again():
    while True:
        choice = input("Would you like to play again? (yes/no): ").strip().lower()
        
        if choice in ['yes', 'y']:
            print("\n" + "-"*60 + "\n")
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.\n")


def main():
    while True:
        play_game()
        
        if not ask_play_again():
            print("\n" + "="*60)
            print("   Thanks for playing the Number Guessing Game!")
            print("          See you next time! 👋")
            print("="*60 + "\n")
            break


if __name__ == "__main__":
    main()
