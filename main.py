import os
import random
from rich.console import Console
from rich.style import Style
from rich.text import Text


def main():
    """
    CLIRDLE: it's wordle in your terminal
    """

    # get the list of words
    with open("words.txt", "r") as f:
        words = f.read().splitlines()

    # choose a random word
    word = random.choice(words).upper()

    # clear the terminal
    os.system("cls" if os.name == "nt" else "clear")

    title = Text("Welcome to CLIRDLE!", style=Style(color="cyan", bold=True))
    console = Console()
    console.print(title)

    style_correct = Style(color="black", bgcolor="green", bold=True)
    style_present = Style(color="black", bgcolor="yellow", bold=True)
    style_absent = Style(color="black", bgcolor="white", bold=True)

    # print the welcome message
    console.print("You have 6 attempts to guess the word.")
    console.print(" ")
    console.print(
        "- [black on green]Green[/black on green]: correct letter in the correct position"
    )
    console.print(
        "- [black on yellow]Yellow[/black on yellow]: correct letter in the wrong position"
    )
    console.print("- [black on white]White[/black on white]: incorrect letter")
    print()

    attempts = 6
    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").upper()

        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue
        
        def space_around(guess):
            list = []
            for i in range(len(guess)):
                list.append(Text(f" {guess[i]} "))
            return list
            #new_string = f" {list[0]}  {list[1]}  {list[2]}  {list[3]}  {list[4]} "
            #return new_string
        feedback_list = space_around(guess)
        #feedback = Text(space_around(guess))
        
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
            console.print("Congratulations! You've guessed the word!")
            break
    else:
        console.print(f"Sorry, you've used all attempts. The word was: {word}")


if __name__ == "__main__":
    main()
