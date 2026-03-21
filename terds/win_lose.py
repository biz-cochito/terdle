import time
import random
from rich.live import Live
from rich.text import Text
from .theme import console
from .terdify import terd_correct, terd_present, terd_absent


# Simple True or False check for win
def is_win(word, guess):
    if word == guess:
        return True
    else:
        return False


def display_win(guess):
    style_funcs = [terd_correct, terd_present, terd_absent]

    def get_flash_frame(final=False):
        text = Text()
        for char in guess:
            if final:
                text.append(terd_correct(char))
            else:
                text.append(random.choice(style_funcs)(char))
        return text

    # 1. Flash the winning word
    with Live(get_flash_frame(), console=console, refresh_per_second=20, transient=False) as live:
        for _ in range(15):
            time.sleep(0.08)
            live.update(get_flash_frame())
        live.update(get_flash_frame(final=True))
        time.sleep(0.5)

    time.sleep(1)

    # 2. Animated reveal of "GOOD JOB!"
    console.print("")
    message = "GOOD JOB!"
    revealed_text = Text()

    with Live(revealed_text, console=console, refresh_per_second=20, transient=False) as live:
        for char in message:
            if char == " ":
                revealed_text.append("   ")
            else:
                revealed_text.append(terd_correct(char))
            live.update(revealed_text)
            time.sleep(0.1)
    console.print("")


def display_lose(word):
    console.print("")
    console.print("No...")
    console.print(f"The word was: {word}")
