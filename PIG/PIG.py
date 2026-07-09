import random


def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


while True:
    player_number = input("enter the number of players (2,4): ")
    if player_number.isdigit():
        player_number = int(player_number)
        if 2 <= player_number <= 4:
            break
        else:
            print('Invalid number, try again')
    else:
        print('Invalid number, try again')

max_score = 70
player_score = [0 for _ in range(player_number)]

while max(player_score) < max_score:
    for player_index in range(player_number):
        print("\nplayer", player_index + 1, "turn has just started\n")

        current_score = 0

        while True:
            should_roll = input('would you like to roll (y)? ').lower()
            if should_roll != "y":
                break
            value = roll()
            if value == 1:
                print('you rolled 1! turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled", value)

            print('your score is:', current_score)

        player_score[player_index] += current_score
        print("your total score is:", player_score[player_index])

        if player_score[player_index] >= max_score:
            break

winning_score = max(player_score)
winner_index = player_score.index(winning_score)
print("\nGame over!")
print("Final scores:", player_score)
print(f"Player {winner_index + 1} wins with {winning_score} points!")
