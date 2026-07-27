import random
from datetime import datetime

MIN_DIE = 1
MAX_DIE = 6
MIN_PLAYERS = 2
MAX_PLAYERS = 6
DEFAULT_TARGET_SCORE = 70
LOG_FILE = "dice_game_log.txt"



def ask_int(prompt, min_value, max_value):
    while True:
        raw = input(prompt)
        if raw.isdigit() and min_value <= int(raw) <= max_value:
            return int(raw)
        print(f"Invalid number, enter a value between {min_value} and {max_value}")


def ask_yes_no(prompt):
    return input(prompt).strip().lower() == "y"



def roll():
    return random.randint(MIN_DIE, MAX_DIE)


class Player:
    def __init__(self, name, is_bot=False, bot_threshold=20):
        self.name = name
        self.is_bot = is_bot
        self.bot_threshold = bot_threshold  
        self.score = 0
        self.rolls_made = 0
        self.ones_rolled = 0
        self.highest_roll_streak = 0  

    def wants_to_roll(self, current_turn_score):
        if self.is_bot:
            return current_turn_score < self.bot_threshold
        return ask_yes_no("would you like to roll (y)? ")


def play_turn(player, target_score):
    """Plays one turn for a player and returns points earned (0 if busted)."""
    current_score = 0
    while player.score + current_score < target_score:
        if not player.wants_to_roll(current_score):
            break
        value = roll()
        player.rolls_made += 1
        if value == 1:
            player.ones_rolled += 1
            print(f"{player.name} rolled 1! Turn done, no points banked.")
            return 0
        current_score += value
        print(f"{player.name} rolled {value} (turn total: {current_score})")
    player.highest_roll_streak = max(player.highest_roll_streak, current_score)
    return current_score


def play_game(players, target_score):
    round_number = 1
    while max(p.score for p in players) < target_score:
        print(f"\n===== Round {round_number} =====")
        for player in players:
            print(f"\n{player.name}'s turn has just started\n")
            gained = play_turn(player, target_score)
            player.score += gained
            print(f"{player.name}'s total score is: {player.score}")
            if player.score >= target_score:
                return players
        round_number += 1
    return players



def setup_players():
    player_count = ask_int(f"enter the number of players ({MIN_PLAYERS}-{MAX_PLAYERS}): ",
                            MIN_PLAYERS, MAX_PLAYERS)
    players = []
    for i in range(player_count):
        if ask_yes_no(f"is player {i + 1} a computer/bot? (y/n): "):
            players.append(Player(f"Bot {i + 1}", is_bot=True))
        else:
            name = input(f"enter a name for player {i + 1}: ").strip() or f"Player {i + 1}"
            players.append(Player(name))
    return players


def setup_target_score():
    if ask_yes_no(f"use default target score of {DEFAULT_TARGET_SCORE}? (y/n): "):
        return DEFAULT_TARGET_SCORE
    return ask_int("enter target score (10-500): ", 10, 500)


# ---------- Results ----------

def print_summary(players):
    print("\nGame over!")
    print("Final scores:")
    for p in players:
        print(f"  {p.name}: {p.score} pts | rolls: {p.rolls_made} | "
              f"1s rolled: {p.ones_rolled} | best turn: {p.highest_roll_streak}")

    winner = max(players, key=lambda p: p.score)
    print(f"\n{winner.name} wins with {winner.score} points!")
    return winner


def save_log(players, winner, target_score):
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- Game played {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        f.write(f"Target score: {target_score}\n")
        for p in players:
            f.write(f"{p.name}: {p.score} pts | rolls: {p.rolls_made} | "
                    f"1s rolled: {p.ones_rolled} | best turn: {p.highest_roll_streak}\n")
        f.write(f"Winner: {winner.name}\n")
    print(f"\nGame log saved to {LOG_FILE}")


# ---------- Main ----------

def main():
    print("=== Dice Game ===")
    target_score = setup_target_score()
    players = setup_players()

    play_again = True
    while play_again:
        for p in players:
            p.score = 0
            p.rolls_made = 0
            p.ones_rolled = 0
            p.highest_roll_streak = 0

        play_game(players, target_score)
        winner = print_summary(players)
        save_log(players, winner, target_score)

        play_again = ask_yes_no("\nplay again with the same players? (y/n): ")

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
