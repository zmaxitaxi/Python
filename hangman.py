import os

##from words import word_list  # Imports the word_list list from different file


def get_word():  # User inputs secret wored
    word = input("Enter your secret word: ").upper()
    print("Secret word is:" + word)
    os.system("cls" if os.name == "nt" else "clear")  # Clears the Terminal
    return word


def play(word):
    word_completion = "_" * len(
        word
    )  # Amount of underscores equals the length of random word
    guessed = False
    guessed_letters = []  # Holds the letters the user gueses
    guessed_words = []  # Holds the words the user guesses
    tries = 6  # Number of tries the user has

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")  # Makes the output easier to read, adds blank line after hangman

    while (
        not guessed and tries > 0
    ):  # Allows guess to input when tries is greater than 0
        guess = input("Please guess a letter or word, your last guess: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)

            elif guess not in word:  # When the guess is incorrect
                print(guess, "is not in the secret word.")
                tries -= 1
                guessed_letters.append(
                    guess
                )  # Adds guessed letter to list, avoid duplicate guesses

            else:  # When guess is correct
                print("Good job,", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(
                    word_completion
                )  # Converts string of underscores and revealed letters into a list
                indices = [
                    i for i, letter in enumerate(word) if letter == guess
                ]  # Creates a list, 'indices', that holds positions that the guessed letter is in
                for index in indices:
                    word_as_list[index] = (
                        guess  # Updates the word list by placing correctly guessed letters in correct positions
                    )
                word_completion = "".join(
                    word_as_list
                )  # Converts the word list back into the string and updates it with all correct letters in correct positions
                if (
                    "_" not in word_completion
                ):  # Checks if there are still underscores for the player to guess
                    guessed = True  # If there are no more underscores, the game ends

        # Guessing words
        elif (
            len(guess) == len(word) and guess.isalpha()
        ):  # Checks if guessed word matches length of the secret word and is a word
            if (
                guess in guessed_words
            ):  # Checks if guessed word is in the string of already guessed words
                print("You already guessed the word", guess)
            elif (
                guess != word
            ):  # If guessed word isn't correct, it deducts tries by one and adds guessed word to a list
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:  # If player guesses the correct word
                guessed = True
                word_completion = word

        else:  # If it doesn't fit any of these criteria, asks the following message
            print("Enter a valid letter or word")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:  # Message when player wins
        print("Congrats, you won")
    else:  # Message when player loses
        print("You lost, the word was" + word + " Maybe next time")


# Hangman display, corresponds with number of tries
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


# Function main gets the word and play functions
def main():
    word = get_word()
    play(word)
    # While loop occurs when game finishes, asks the user if it wants to play again
    while input("Play Again?(Y/N)").upper() == "Y":
        word = get_word()
        play(word)


# Ensures main function is called when script is run directly
if __name__ == "__main__":
    main()
