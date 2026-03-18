import shutil
import string
from rich.text import Text
from .theme import console

def draw_alphabet(absent_letters: set[str]):
    cols, lines = shutil.get_terminal_size()
    if lines < 20:
        return

    first_half = Text()
    for letter in string.ascii_uppercase[:13]:
        if letter in absent_letters:
            first_half.append(f" {letter} ", style="dim")
        else:
            first_half.append(f" {letter} ")

    second_half = Text()
    for letter in string.ascii_uppercase[13:]:
        if letter in absent_letters:
            second_half.append(f" {letter} ", style="dim")
        else:
            second_half.append(f" {letter} ")

    # Save cursor, move to third-to-last line, clear line
    print(f"\033[s\033[{lines-2};0H\033[K", end="")
    console.print(first_half, justify="center", end="")

    # Move to second-to-last line, clear line
    print(f"\033[{lines-1};0H\033[K", end="")
    console.print(second_half, justify="center", end="")

    # Restore cursor
    print("\033[u", end="", flush=True)

def clear_alphabet():
    cols, lines = shutil.get_terminal_size()
    if lines < 20:
        return
        
    print(f"\033[s\033[{lines-2};0H\033[K\033[{lines-1};0H\033[K\033[u", end="", flush=True)
