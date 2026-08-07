# Tic-Tac-Toe (vs. Unbeatable AI)

A terminal-based Tic-Tac-Toe game written in Python. The AI opponent uses the
**minimax algorithm**, so it plays perfectly — the best you can do is force a
draw.

## Features

- Unbeatable AI opponent (minimax search)
- Randomized AI opening move for variety
- Choose to go first or second
- Input validation (rejects out-of-range or already-taken moves)
- Replay loop — play as many rounds as you like

## Requirements

- Python 3.7+
- No external dependencies (uses only the standard library)

## How to Run

```bash
python tic_tac_toe.py
```

## How to Play

1. When prompted, choose whether you want to go first (`y`/`n`).
2. The board positions are numbered 1–9, left to right, top to bottom:

   ```
   1 | 2 | 3
   ---+---+---
   4 | 5 | 6
   ---+---+---
   7 | 8 | 9
   ```

3. Enter a number to place your mark (`X`) in that position.
4. The AI (`O`) will respond automatically.
5. The game announces a winner or a draw at the end of each round.
6. You'll be asked if you want to play again.

## How the AI Works

The AI evaluates every possible sequence of remaining moves using **minimax**:

- It recursively simulates all possible games from the current position.
- Wins for the AI score positively, wins for the human score negatively, and
  draws score zero — with faster wins/losses weighted more heavily.
- The AI always picks the move that maximizes its guaranteed outcome,
  assuming the human also plays optimally.

Because Tic-Tac-Toe is a "solved" game, perfect play from both sides always
ends in a draw — so the AI can never be beaten, only tied.

## Project Structure

```
tic_tac_toe.py   # Game logic, AI, and terminal interface
README.md        # This file
```

## Possible Extensions

- Add a difficulty setting (let the AI occasionally play suboptimally)
- Build a GUI version (e.g. with `tkinter` or `pygame`)
- Support larger boards (e.g. 4x4, 5x5) with a win-length rule
- Add a scoreboard that persists across rounds
