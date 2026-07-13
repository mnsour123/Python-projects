# Math Quiz

A simple terminal quiz that gives you random math problems and times how long it takes to finish them all.

## Run it

```bash
python Mathquestions.py
```

## How it works

- Generates 10 random problems using `+`, `-`, and `*` with operands between 3 and 12.
- Each problem repeats until you enter the correct answer.
- After the last problem, it prints your total time and number of wrong guesses.

## Customize

Edit these constants at the top of the file:

| Constant | Purpose |
|---|---|
| `OPERATORS` | Which math operations to use |
| `MIN_OPERAND` / `MAX_OPERAND` | Range for the random numbers |
| `TOTAL_PROBLEMS` | How many problems per round |
