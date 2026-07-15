# Math Quiz

A simple command-line arithmetic quiz. Answer 10 random problems (addition,
subtraction, multiplication, and division) and get a summary of your speed
and accuracy at the end.

## Usage

```bash
python math_quiz.py
```

1. Pick a difficulty level (Easy, Medium, or Hard) — this controls the
   range of numbers used in each problem.
2. Press Enter to start.
3. Answer each problem. If you get it wrong, you'll be asked to try again
   until you answer correctly.
4. Type `q` at any prompt to quit early.

## Features

- **Four operators**: `+`, `-`, `*`, `/`
  - Division problems always divide evenly (no decimals).
  - Subtraction problems never produce a negative result.
- **Difficulty levels**: choose the number range for the problems.
- **Input validation**: non-numeric input is rejected with a friendly
  message instead of crashing or silently counting as wrong.
- **Quit anytime**: type `q` during the quiz to exit cleanly.
- **End-of-quiz summary**:
  - Total time taken
  - Total wrong guesses
  - First-try accuracy (% of problems solved correctly on the first
    attempt)
  - Average time per problem

## Example

```
Choose a difficulty:
  1) Easy  (operands 3-10)
  2) Medium  (operands 3-12)
  3) Hard  (operands 5-20)
> 2

Medium mode selected. Press enter to start (or type "q" during the quiz to quit)
---------------------
Problem #1: 7 * 9 =
```

## Possible future improvements

- Allow negative results for subtraction as an optional mode
- Add a per-question timer
- Let difficulty also control which operators appear
- Save high scores to a file
