from rich.text import Text
from .theme import style_correct, style_present, style_absent


# convert string to terd (list of Text objects with spaces around)
def terdify(string):
    terd = []
    for i in range(len(string)):
        terd.append(Text(f" {string[i]} "))
    return terd


def terd_correct(word):
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


def terd_present(word):
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


def terd_absent(word):
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
