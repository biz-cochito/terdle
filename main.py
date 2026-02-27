import os
import random
from rich.console import Console
from rich.style import Style
from rich.text import Text
from terdle_funcs import space_around, color_blocks


def main():
    """
    TERDLE: wordle in your terminal
    """
    with open("words.txt", "r") as f:
        words = f.read().splitlines()

    word = random.choice(words).upper()

    os.system("cls" if os.name == "nt" else "clear")

    title = Text("Welcome to TERDLE", style=Style(color="cyan", bold=True))
    console = Console()
    console.print(title)

    style_correct = Style(color="black", bgcolor="green", bold=True)
    style_present = Style(color="black", bgcolor="yellow", bold=True)
    style_absent = Style(color="black", bgcolor="white", bold=True)

    console.print("You have 6 attempts to guess the word.")
    console.print("- [black on green]Green[/black on green]: correct letter in the correct position")
    console.print("- [black on yellow]Yellow[/black on yellow]: correct letter in the wrong position")
    console.print("- [black on white]White[/black on white]: incorrect letter")
    # print()

    def display_win():
        console.print("")
        console.print(color_blocks(space_around("GOOD JOB"), 22222))
    def display_lose():
        console.print("")
        console.print("No...")
        console.print(f"The word was: {word}").stylize(style_absent)
    
    attempts = 6
    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").upper()

         
        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue

        feedback_list = space_around(guess)

        # Check for win first
        if guess == word:
            for i in range(len(word)):
                feedback_list[i].stylize(style_correct)
            feedback = Text()

            for item in feedback_list:
                feedback += item

            console.print(feedback)
            display_win()
        else:
            for i in range(len(word)):
                if guess[i] == word[i]:
                    feedback_list[i].stylize(style_correct)
                elif guess[i] in word:
                    feedback_list[i].stylize(style_present)
                else:
                    feedback_list[i].stylize(style_absent)

            feedback = Text()

            for item in feedback_list:
                feedback += item

            console.print(feedback)

    if guess == word:
            display_win()
    else:
        console.print("")
        console.print("No...")
        console.print(f"The word was: {word}")


if __name__ == "__main__":
    main()
