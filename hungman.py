import random
# List of words
words = ["python", "computer", "program", "coding", "electronics"]
# Select a random word
word = random.choice(words)
# Store guessed letters
guessed_letters = []
# Number of wrong guesses
wrong_guesses = 0
# Maximum wrong guesses
max_wrong_guesses = 6
print("================================")
print("       HANGMAN GAME")
print("================================")
# Game loop
while wrong_guesses < max_wrong_guesses:
    # Display the word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    # Check if word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You won!")
        break
    # Get user's guess
    guess = input("Enter a letter: ").lower()
    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    # Add guess to list
    guessed_letters.append(guess)
    # Check guess
    if guess in word:
        print("Correct guess! 👍")
    else:
        wrong_guesses += 1
        print("Wrong guess! ❌")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
else:
    print("\nGame Over! ❌")
    print("The word was:", word)