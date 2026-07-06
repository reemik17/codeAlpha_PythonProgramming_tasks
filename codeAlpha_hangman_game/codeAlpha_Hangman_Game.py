import random

# List of predefined words
fruits = ["apple", "banana", "orange", "strawberry", "mango"]

# Select a random word
random_word = random.choice(fruits)

# Variables
guessed_letters = []
incorrect_guesses = 0
maximum_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the fruit one letter at a time.")

# Game loop
while incorrect_guesses < maximum_incorrect_guesses:

    # Display the word with guessed letters
    display_word = ""

    for letter in random_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)

    # Check if the player has guessed the whole word
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", random_word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in random_word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Incorrect!")
        print("Remaining attempts:", maximum_incorrect_guesses - incorrect_guesses)

# Game over
if incorrect_guesses == maximum_incorrect_guesses:
    print("Game Over!")
    print("The word was:", random_word)