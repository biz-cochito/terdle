from rich.console import Console
from rich.style import Style
from rich.text import Text

def space_around(guess):
    list = []
    for i in range(len(guess)):
        list.append(Text(f" {guess[i]} "))
    return list

# define the coloring with an int where each digit determines
# the color of the corresponding item in the text
# 0- white, 1- yellow, 2- green (e.g., 20210 = green, white, green, yellow, white)
def color_blocks(text, color_code):
    style_correct = Style(color="black", bgcolor="green", bold=True)
    style_present = Style(color="black", bgcolor="yellow", bold=True)
    style_absent = Style(color="black", bgcolor="white", bold=True)

    result = Text()
    for i, char in enumerate(text):
        if i < len(str(color_code)):
            color_digit = int(str(color_code)[i])
            if color_digit == 2:
                result.append(char, style=style_correct)
            elif color_digit == 1:
                result.append(char, style=style_present)
            else:
                result.append(char, style=style_absent)
        else:
            result.append(char, style=style_absent)
    return result