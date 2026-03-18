![Terdle Title](images/title.gif)

# TERDLE

## Installation
```bash
git clone https://github.com/biz-cochito/terdle.git
cd terdle
uv sync
```

Run the game with `uv run main.py`.

## To do

### Game logic
- [x] correct handling of duplicate letters
- [x] restrict guesses to valid words
- [x] separate word lists for valid guesses and potential target words

### UI
- [x] start menu
- [x] title animation
- [x] display available letters
- [ ] center terminal output
- [ ] animate win message

### Input
- [x] allow cursor movement with arrow keys on guess input
- [ ] "?" key to show keyboard shortcuts
- [ ] keyboard shortcut to exit the game
- [ ] keyboard shortcut to return to the main menu

### Settings and configuration
- [ ] color themes
- [ ] choose word length

### Stats
- [ ] win/loss ratio
- [ ] current winning streak
- [ ] longest winning streak
- [ ] guess distribution
- [ ] average guesses
- [ ] total games played

