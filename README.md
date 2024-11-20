# Hangman Game

Welcome to the **Hangman Game**, a classic word-guessing game implemented in Python! This project allows players to guess a secret word by guessing one letter at a time, with a limited number of wrong guesses allowed. Have fun!

---

## How to Play

1. The program will choose a secret word from a text file based on an index provided by the user.
2. Players guess one letter at a time.
3. Each correct guess reveals the letter's position(s) in the word.
4. Each wrong guess brings the player closer to losing and updates the hangman drawing.
5. The game ends when:
   - The player successfully guesses the entire word (**YOU WIN**).
   - The player exceeds the maximum allowed attempts (**YOU LOSE**).

---

## Features

- **Dynamic hangman visuals**: The hangman evolves with each incorrect guess.
- **Encouragement and Success Messages**: Players receive motivational messages based on their progress.
- **Customizable secret word**: Load words from a text file for endless fun.
- **Replay option**: Choose to play again or end the game after finishing a round.

---

### Prerequisites
- A text file containing a list of words.

---

## **Code Highlights**

**Key Constants:**

HANGMAN_PHOTOS: Contains ASCII art for each stage of the hangman.
MAX_TRIES: Maximum number of incorrect attempts allowed (default is 6).

**Functions:**

openScreen(): Displays a welcome screen with ASCII art.

choose_word(file_path, index): Selects a word from a file based on the index.

check_win(secret_word, old_letters_guessed): Checks if the player has guessed the word.

show_hidden_word(secret_word, old_letters_guessed): Displays the current progress with underscores for unguessed letters.

try_update_letter_guessed(letter_guessed, old_letters_guessed): Validates and processes a guessed letter.
