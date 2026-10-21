import random

words = ["python", "coding", "computer", "program", "developer"]

secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("\n===== WELCOME TO HANGMAN =====")
print("Guess the hidden word one letter at a time!")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_attempts:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The correct word is:", secret_word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

if incorrect_guesses == max_attempts:
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)
