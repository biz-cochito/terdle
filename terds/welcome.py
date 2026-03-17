from .theme import console


def welcome():
    console.print("You have 6 attempts to guess the word.")
    console.print(
        "- [black on green] G R E E N [/black on green]: correct letter in the correct position"
    )
    console.print(
        "- [black on yellow] Y E L L O W [/black on yellow]: correct letter in the wrong position"
    )
    console.print("- [black on white] W H I T E [/black on white]: incorrect letter")
    console.print(" ")
