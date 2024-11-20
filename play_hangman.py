import random
HANGMAN_PHOTOS = {1: "x-------x",
                  2: """
                        x-------x
                        |
                        |
                        |
                        |
                        |
                    """,
                  3: """
                        x-------x
                        |       |
                        |       0
                        |
                        |
                        |
                  """,
                  4: """
                        x-------x
                        |       |
                        |       0
                        |       |
                        |
                        |
                  """,
                  5: """
                        x-------x
                        |       |
                        |       0
                        |      /|\\
                        |
                        |
                  """,
                  6: """
                        x-------x
                        |       |
                        |       0
                        |      /|\\
                        |      /
                        |
                  """,
                  7: """
                        x-------x
                        |       |
                        |       0
                        |      /|\\
                        |      / \\
                        |
                  """
                  }
MAX_TRIES = 6
def openScreen():
    """
    opem screen
    :return: none
    """
    HANGMAN_ASCII_ART = ("""Welcome to the game Hangman
                           _    _
                          | |  | |
                          | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
                          |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
                          | |  | | (_| | | | | (_| | | | | | | (_| | | | |
                          |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                                                 __/ |
                                                |___/\n""")
    print(HANGMAN_ASCII_ART, "you have", MAX_TRIES, "attempts")
def print_hangman(num_of_tries):
    """
    Print one of the Hanged Man status images, depending on the number of wrong guesses the player made.
    :param num_of_tries: The number of failed attempts by the user so far
    :return: none
    """
    print(HANGMAN_PHOTOS[num_of_tries])
def choose_word(file_path, index):
    """
    Choosing a word from the file to be guessed by the player
    :param file_path: Path to the text file
    :param index: Position of a particular word in the file
    :return: the word in the position received as an argument to the function
    """
    with open(file_path, 'r') as file:
        words = file.read().split()
    unique_words = set(words)
    adjusted_index = (index - 1) % len(words)
    secret_word = words[adjusted_index]
    return secret_word
def check_win(secret_word, old_letters_guessed):
    """
    Checking whether the player managed to guess the secret word and thus won the game
    :param secret_word: The string represents the secret word that the player has to guess.
    :param old_letters_guessed: The list contains the letters the player has guessed so far.
    :return: true if all the letters that make up the secret word are included
    in the list of letters that the user guessed. Otherwise, the function returns false.
    """
    for l in secret_word:
        if l not in old_letters_guessed:
            return False
    return True
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The function returns false If letter_guessed consists of two or more characters or
    contains a character that is not an English letter or is a character that is already in the list old_letters_guessed
    and returns true if letter_guessed consists of only one letter that is an
    English letter that is not in the list old_letters_guessed
    :param letter_guessed: The character received from the player
    :param old_letters_guessed: The list contains the letters the player has guessed so far
    :return: True if the string is valid, false otherwise
    """
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    return True
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    If the character is correct and it was not guessed before, we will add the character to the list and it will return true,
    If the letter is incorrect or is already in the guessed list, we will print X and below it
    the list old_letters_guessed and it will return false
    :param letter_guessed: The character received from the player
    :param old_letters_guessed: A list containing the letters the player has guessed so far
    :return: True if the addition was successful, false if the character cannot be added to the list of already guessed characters.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        sorted_guesses = " -> ".join(sorted(old_letters_guessed))
        print(sorted_guesses)
        return False
def show_hidden_word(secret_word, old_letters_guessed):
    """
    Player progress in the game
    :param secret_word: The string represents the secret word that the player has to guess.
    :param old_letters_guessed: The list contains the letters the player has guessed so far.
    :return:A string consisting of letters and underscores.
            The string shows the letters from the old_letters_guessed list that are in the secret_word string in their
            appropriate position, and the other letters in the string (which the player has not yet guessed) as underlines.
    """
    str = ""
    for l in secret_word:
        if l in old_letters_guessed:
            str += l + " "
        else:
            str += "_ "

    return str.strip()

def main():
    while True:
        num_of_tries = 1
        old_letters_guessed = []
        success_messages = [
            ":)",
            "You're doing great!",
            "Well done, keep it up!",
            "Fantastic job!",
            "You're amazing!",
            "You're on fire!",
            "Excellent work!",
            "You're crushing it!",
            "Keep it up, you're so close!",
            "You're a pro!",
            "Great job, you're getting better!"
        ]
        encouragement_messages = [
            ":(",
            "Don't give up!",
            "Keep going, you'll get it!",
            "Try again, you can do it!",
            "No worries, just one more try!",
            "You're almost there, don't stop!",
            "Failure is just a step toward success!",
            "It’s okay, everyone makes mistakes!",
            "You're doing great, just a little more!",
            "Keep trying, you're improving!",
            "Stay positive, you’re getting closer!"
        ]

        openScreen()
        file_path = input("please enter file path: ")
        index = int(input("please enter index: "))
        secret_word = choose_word(file_path, index)
        print("\nlet's start!\ngood luck:)\n")
        print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))

        while num_of_tries <= MAX_TRIES:
            ch = input("Guess a letter: ")
            if not try_update_letter_guessed(ch, old_letters_guessed):
                continue
            if ch in secret_word:
                # Check if the player has guessed the entire word
                if check_win(secret_word, old_letters_guessed):
                    print(show_hidden_word(secret_word, old_letters_guessed))
                    print("YOU WIN!!!")
                    break # Stop the loop if the player wins
                print(show_hidden_word(secret_word, old_letters_guessed))
                print(random.choice(success_messages)+"\n")

            else:
                num_of_tries += 1
                print(random.choice(encouragement_messages))
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))

        # If the loop ended and the player didn't guess the word
        if not check_win(secret_word, old_letters_guessed):
            print("you lose :(\ntry again\n")

        #Check if you want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()