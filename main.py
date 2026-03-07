import os
import random
from rich.console import Console
from rich.style import Style
from rich.text import Text
from terds import *
from terds import welcome


def load_words(file_path):
    with open(file_path, "r") as f:
        words = [line.strip() for line in f if len(line.strip()) == 5]
    return words


def welcome():
    console = Console()
    title = Text("TERDLE", style="bold white on cyan")
    console.print(title)
    console.print("You have 6 attempts to guess the word.")
    console.print(
        "- [black on green]Green[/black on green]: correct letter in the correct position"
    )
    console.print(
        "- [black on yellow]Yellow[/black on yellow]: correct letter in the wrong position"
    )
    console.print("- [black on white]White[/black on white]: incorrect letter")
    # print()


def main():
    words = load_words("words.txt")
    word = random.choice(words).upper()

    console = Console()

    welcome()

    os.system("cls" if os.name == "nt" else "clear")

    attempts = 6
    attempt = 0
    while attempt < attempts:
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").upper()

        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue

        attempt += 1

        feedback = score_guess(word, guess)
        console.print(feedback)

        if is_win(word, guess):
            display_win()
            break
    else:
        display_lose(word)


if __name__ == "__main__":
    main()
