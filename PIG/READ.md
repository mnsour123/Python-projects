# Dice Game

A simple turn-based push-your-luck dice game for 2–6 players, playable against friends or computer-controlled bots.

## How to Play

Each turn, roll a die as many times as you like, adding up the values as you go.

- Roll a **1** and you lose all the points from that turn (bust).
- Choose to **stop** at any time and bank your current turn total to your overall score.
- First player to reach the **target score** (default: 70) wins.

## Requirements

- Python 3.6+
- No external dependencies (standard library only)

## Running the Game

```bash
python3 dice_game.py
```

You'll be prompted to:

1. Set a target score (or use the default of 70)
2. Choose the number of players (2–6)
3. For each player, decide if they're human or a bot, and name them

During your turn, type `y` and press Enter to roll, or anything else to bank your points and pass the turn.

## Bots

Bot players roll automatically until their turn total reaches a threshold (default: 20 points), then stop on their own. No input needed on their turns.

To change bot behavior, edit the `bot_threshold` value when creating a `Player` in `setup_players()`:

```python
players.append(Player(f"Bot {i + 1}", is_bot=True, bot_threshold=20))
```

Lower the threshold for a more cautious bot, raise it for a riskier one.

## Game Log

After each game, results are appended to `dice_game_log.txt` in the same folder, including:

- Timestamp
- Target score
- Each player's final score, total rolls, number of 1s rolled, and best single-turn score
- The winner

This file is created automatically the first time you play and grows with each subsequent game.

## Replaying

At the end of a game, you'll be asked if you want to play again with the same players. Scores and stats reset, but player names and bot settings carry over.

## File Overview

| File | Description |
|---|---|
| `dice_game.py` | Main game script |
| `dice_game_log.txt` | Auto-generated log of past games (created after your first playthrough) |
