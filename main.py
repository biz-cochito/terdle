import random
import readline
import terds
from util.shell_commands import clear_terminal
import questionary

def load_words(file_path):
    with open(file_path, "r") as f:
        words = [line.strip() for line in f if len(line.strip()) == 5]
    return words

def play_game():
    words = load_words("word-lists/5-letters.txt")
    valid_guesses = load_words("word-lists/5-valid.txt")
    
    valid_words = set(w.upper() for w in words + valid_guesses)
    word = random.choice(words).upper()

    clear_terminal()

    terds.animate_title()
    terds.welcome()

    attempts = 6
    attempt = 0
    while attempt < attempts:
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").upper()

        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue

        if guess not in valid_words:
            print("Invalid word. Please try again.")
            continue

        attempt += 1

        feedback = terds.score_guess(word, guess)
        terds.console.print(feedback)

        if terds.is_win(word, guess):
            terds.display_win()
            break
    else:
        terds.display_lose(word)
        
    input("Press Enter to return to the main menu...")

def show_settings():
    clear_terminal()
    terds.animate_title()
    terds.console.print("\n[bold yellow]Settings menu coming soon...[/bold yellow]")
    input("\nPress Enter to return to the main menu...")

def main():
    while True:
        clear_terminal()
        terds.animate_title()
        
        terds.console.print("[bold cyan]--- Main Menu ---[/bold cyan]")
        
        custom_style = questionary.Style([
            ('instruction', 'fg:#808080')
        ])
        
        choice = questionary.select(
            "",
            choices=[
                "Play",
                "Settings",
                "Quit"
            ],
            qmark="?",
            pointer=">",
            instruction="(Use arrow keys to move, Enter to select)",
            style=custom_style
        ).ask()
        
        if choice == 'Play':
            play_game()
        elif choice == 'Settings':
            show_settings()
        elif choice == 'Quit' or choice is None: # None if user presses Ctrl+C
            clear_terminal()
            terds.console.print("[bold green]Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main()
