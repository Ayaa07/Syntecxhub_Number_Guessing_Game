import random

def get_max_range():
    print("\nDifficulty Levels ")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    
    choice = input("Select difficulty (1-3): ").strip()
    if choice == '1':
        return 50
    elif choice == '3':
        return 200
    return 100  

def play_game(best_score):
    max_range = get_max_range()
    target = random.randint(1, max_range)
    attempts = 0

    print(f"\nGuess the number between 1 and {max_range}!")

    while True:
        user_input = input("Enter your guess: ").strip()
        
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f" Correct! You won in {attempts} attempts.")
            
            if best_score is None or attempts < best_score:
                best_score = attempts
                print(" New Best Score!")
            break

    print(f"Best Score: {best_score} attempt(s)")
    return best_score

def main():
    print("NUMBER GUESSING GAME")
    best_score = None
    
    while True:
        best_score = play_game(best_score)
        
        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break

