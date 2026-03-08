from rich.console import Console
from rich.style import Style
from rich.text import Text
from collections import Counter

console = Console()

style_correct = Style(color="black", bgcolor="green", bold=True)
style_present = Style(color="black", bgcolor="yellow", bold=True)
style_absent = Style(color="black", bgcolor="white", bold=True)


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


# convert string to terd (list of Text objects with spaces around)
def terdify(string):
    terd = []
    for i in range(len(string)):
        terd.append(Text(f" {string[i]} "))
    return terd


# Simple True or False check for win
def is_win(word, guess):
    if word == guess:
        return True
    else:
        return False


def terd_green(word):
    style_correct = Style(color="black", bgcolor="green", bold=True)
    if isinstance(word, list):
        terd = Text()
        for block in word:
            block.stylize(style_correct)
            terd.append(block)
        return terd
    elif isinstance(word, Text):
        terd = Text(word.plain)
        terd.stylize(style_correct)
        return terd
    else:
        terd = Text(f" {word} ")
        terd.stylize(style_correct)
        return terd


def terd_yellow(word):
    style_present = Style(color="black", bgcolor="yellow", bold=True)
    if isinstance(word, list):
        terd = Text()
        for block in word:
            block.stylize(style_present)
            terd.append(block)
        return terd
    elif isinstance(word, Text):
        terd = Text(word.plain)
        terd.stylize(style_present)
        return terd
    else:
        terd = Text(f" {word} ")
        terd.stylize(style_present)
        return terd


def terd_white(word):
    style_absent = Style(color="black", bgcolor="white", bold=True)
    if isinstance(word, list):
        terd = Text()
        for block in word:
            block.stylize(style_absent)
            terd.append(block)
        return terd
    elif isinstance(word, Text):
        terd = Text(word.plain)
        terd.stylize(style_absent)
        return terd
    else:
        terd = Text(f" {word} ")
        terd.stylize(style_absent)
        return terd


def score_guess(word, guess):
    letter_count = Counter(word)
    feedback = [None] * len(word)
    feedback_terd = Text()

    # Pass 1: find exact matches (Green)
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback[i] = terd_green(guess[i])
            letter_count[guess[i]] -= 1

    # Pass 2: find present but wrong position (Yellow) and absent (White)
    for i in range(len(word)):
        if feedback[i] is None:
            if guess[i] in word and letter_count[guess[i]] > 0:
                feedback[i] = terd_yellow(guess[i])
                letter_count[guess[i]] -= 1
            else:
                feedback[i] = terd_white(guess[i])

    for item in feedback:
        feedback_terd.append(item)
    return feedback_terd


def display_win():
    console.print("")
    console.print(terd_green("G O O D  J O B !"))


def display_lose(word):
    console.print("")
    console.print("No...")
    console.print(f"The word was: {word}")
