from .theme import console
from .terdify import terd_green


# Simple True or False check for win
def is_win(word, guess):
    if word == guess:
        return True
    else:
        return False


def display_win():
    console.print("")
    console.print(terd_green("G O O D  J O B !"))


def display_lose(word):
    console.print("")
    console.print("No...")
    console.print(f"The word was: {word}")
