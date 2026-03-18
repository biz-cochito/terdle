import time
import random
from rich.text import Text
from rich.live import Live
from .theme import console
from .terdify import terd_correct, terd_present, terd_absent


def animate_title():
    title_str = "TERDLE"
    style_funcs = [terd_correct, terd_present, terd_absent]

    def get_frame(final=False):
        text = Text()
        for char in title_str:
            if final:
                text.append(terd_correct(char))
            else:
                text.append(random.choice(style_funcs)(char))
        return text

    with Live(
        get_frame(), console=console, refresh_per_second=20, transient=False
    ) as live:
        # play animation for about 1.5 seconds
        for _ in range(20):
            time.sleep(0.08)
            live.update(get_frame())

        # settle on all green
        live.update(get_frame(final=True))
        time.sleep(0.5)
    console.print()
