import random

# Define word categories
word_categories = {
    "fruits": ["apple", "banana", "orange", "grape", "strawberry", "watermelon"],
    "animals": ["elephant", "tiger", "giraffe", "zebra", "monkey", "penguin"],
    "countries": ["america", "canada", "japan", "brazil", "china", "india"]
}

def choose_word(category):
    words = word_categories.get(category)
    if words:
        return random.choice(words)
    else:
        return None

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    while True:
        category = input("Choose a category (fruits, animals, countries): ").lower()
        if category in word_categories:
            break
        else:
            print("Invalid category! Please choose from fruits, animals, or countries.")

    word = choose_word(category)
    if not word:
        print("Error: No words found in the selected category.")
        return

    guessed_letters = []
    attempts = 6

    print("\nThe word has", len(word), "letters.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            attempts -= 1
            if attempts == 0:
                print("You ran out of attempts! The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing Hangman!")
    else:
        hangman()

if __name__ == "__main__":
    hangman()
# Write your code here :-)
