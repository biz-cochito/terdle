# TERDLE

## Installation

**Using pip w/ venv**
```bash
git clone https://github.com/bis-1/terdle.git
cd terdle
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Using uv**
```bash
git clone https://github.com/bis-1/terdle.git
cd terdle
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Running the Game

In the `terdle` directory, activate your virtual environment:
- **Linux/macOS:** `source .venv/bin/activate`
- **Windows:** `.venv\Scripts\activate`

Run the game with `python main.py` or `uv run main.py`.

## To do

- [ ] allow cursor movement with arrow keys on guess input
- [x] start menu
- [ ] alternative color settings for terminals with incompatible color schemes
- [x] title animation
- [ ] different word-length modes
- [ ] restrict guesses to valid words
- [ ] separate word lists for valid guesses and potential target words
- [ ] keyboard shortcut to exit the game
- [ ] keyboard shortcut to return to the main menu