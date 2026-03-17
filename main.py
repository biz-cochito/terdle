import random
import terds
from util.shell_commands import clear_terminal


def load_words(file_path):
    with open(file_path, "r") as f:
        words = [line.strip() for line in f if len(line.strip()) == 5]
    return words


def main():
    words = load_words("words.txt")
    word = random.choice(words).upper()

    clear_terminal()

    terds.animate_title()
    terds.welcome()

    attempts = 6
    attempt = 0
    while attempt < attempts:
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").upper()

        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue

        attempt += 1

        feedback = terds.score_guess(word, guess)
        terds.console.print(feedback)

        if terds.is_win(word, guess):
            terds.display_win()
            break
    else:
        terds.display_lose(word)


if __name__ == "__main__":
    main()
