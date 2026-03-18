from .theme import console


def welcome():
    console.print("You have 6 attempts to guess the word.")
    console.print(
        "[black on green]  CORRECT  [/black on green] - correct letter in the correct position"
    )
    console.print(
        "[black on yellow] MISPLACED [/black on yellow] - correct letter in the wrong position"
    )
    console.print("[black on white] INCORRECT [/black on white] - incorrect letter\n")
