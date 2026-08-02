#  Math Quiz

A command-line arithmetic quiz game written in Python. Pick a difficulty, solve randomly generated problems, and get a full breakdown of your speed, accuracy, and streaks at the end.

## Features

- Three difficulty levels (Easy / Medium / Hard) with different operand ranges
- Choose how many problems you want per round
- Covers addition, subtraction, multiplication, and division
- Division problems always divide evenly (no messy decimals)
- Subtraction never produces negative results
- Retry until you get each problem right — wrong attempts are tracked
- End-of-round stats: total time, accuracy, average time per problem, best streak
- Per-operator breakdown so you can see which operation you're weakest at
- Quit anytime mid-quiz by typing `q`
- Play multiple rounds in a row without restarting the script

## Requirements

- Python 3.x

No external libraries needed — only the Python standard library (`random`, `time`, `operator`).

## How to Run

```bash
python math_quiz.py
```

On some systems you may need `python3` instead of `python`.

## How to Play

1. Choose a difficulty (`1`, `2`, or `3`).
2. Choose how many problems you'd like, or press Enter for the default (10).
3. Press Enter to start.
4. Type your answer to each problem and press Enter.
   - If you're wrong, you'll be asked to try the same problem again.
   - Type `q` at any point to quit early.
5. After the last problem, you'll see your results:
   - Total time taken
   - Number of wrong guesses
   - First-try accuracy
   - Average time per problem
   - Best streak of consecutive first-try answers
   - A breakdown of first-try accuracy by operator
6. Choose whether to play another round.

## Difficulty Levels

| Level  | Operand Range |
|--------|---------------|
| Easy   | 3–10          |
| Medium | 3–12          |
| Hard   | 5–20          |

## Customizing

- Add or adjust difficulty levels by editing the `DIFFICULTIES` dictionary.
- Add new operators by extending the `OPERATORS` dictionary with another `operator` module function.
- Change the default problem count via `DEFAULT_PROBLEM_COUNT`.

## File Structure

```
math_quiz.py   # main game script — just run this
README.md      # this file
```
