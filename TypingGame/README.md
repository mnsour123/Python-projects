# ⌨ Typing Speed Game

A simple desktop typing speed test built with Python's Tkinter — type the given paragraph as fast and accurately as you can, then see your WPM (words per minute) and accuracy score.

## Features

- Random paragraph prompts each round
- Live timer while you type
- WPM calculated using the standard formula (characters ÷ 5, per minute)
- Word-by-word accuracy scoring
- Restart anytime for a new paragraph
- Clean dark-mode UI, no external dependencies

## Requirements

- Python 3.x
- Tkinter (included with most standard Python installations)

No `pip install` needed — everything used is part of the Python standard library.

## How to Run

```bash
python typing_game.py
```

On some systems you may need `python3` instead of `python`.

## How to Play

1. Click **Start**.
2. Type the displayed paragraph into the text box as quickly and accurately as you can.
3. Press **Enter** (or click **Finish**) when you're done.
4. Your time, WPM, and accuracy will be displayed.
5. Click **Restart** to try again with a new random paragraph.

## Customizing Paragraphs

Add your own text prompts by editing the `paragraphs` list near the top of `typing_game.py`:

```python
paragraphs = [
    "Your custom sentence here.",
    "Another one to practice with.",
]
```

## File Structure

```
typing_game.py   # main game script — just run this
README.md        # this file
```

## Notes

- Accuracy is scored by comparing your typed words to the target words in order — a missed or extra word will shift the rest, similar to how most typing tests work.
- WPM uses time elapsed from clicking **Start** to pressing **Enter**/**Finish**.
