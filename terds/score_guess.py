from collections import Counter
from rich.text import Text
from .terdify import terd_correct, terd_present, terd_absent


def score_guess(word, guess):
    letter_count = Counter(word)
    feedback = [None] * len(word)
    feedback_terd = Text()

    # pass 1: find exact matches (green)
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback[i] = terd_correct(guess[i])
            letter_count[guess[i]] -= 1

    # pass 2: find present but wrong position (yellow) and absent (white)
    for i in range(len(word)):
        if feedback[i] is None:
            if guess[i] in word and letter_count[guess[i]] > 0:
                feedback[i] = terd_present(guess[i])
                letter_count[guess[i]] -= 1
            else:
                feedback[i] = terd_absent(guess[i])

    for item in feedback:
        feedback_terd.append(item)
    return feedback_terd
