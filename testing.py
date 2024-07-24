import random

# Function to generate a hint based on the secret word and the user's guess
def generate_hint(secret_word, user_guess):
    hint = ""
    for i in range(len(secret_word)):
        if user_guess[i] == secret_word[i]:
            hint += user_guess[i].upper()  # If the letter is in the correct position
        elif user_guess[i] in secret_word:
            hint += user_guess[i].lower()  # If the letter is in the word but not in the right position
        else:
            hint += "_"  # If the letter is not in the word
    return hint

# Main function for the game
def word_guessing_game(secret_word):
    print("Welcome to the word guessing game!")
    print("Your hint is:", "_" * len(secret_word))

    guesses = 0
    while True:
        user_guess = input("What is your guess? ").lower()  # Convert guess to lowercase
        if len(user_guess) != len(secret_word):
            print("Your guess should have the same number of letters as the secret word.")
            continue

        guesses += 1

        if user_guess == secret_word:
            print("Congratulations! You guessed it!")
            print("It took you", guesses, "guesses.")
            break
        else:
            hint = generate_hint(secret_word, user_guess)
            print("Your hint is:", hint)

# Secret word for the game
secret_word = "lifegate"

# Start the game
word_guessing_game(secret_word)