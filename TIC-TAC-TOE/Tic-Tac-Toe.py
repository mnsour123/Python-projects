import math
import random

HUMAN = "X"
AI = "O"
EMPTY = " "


def new_board():
    return [EMPTY] * 9


def print_board(board):
    rows = [board[i:i + 3] for i in range(0, 9, 3)]
    print()
    for i, row in enumerate(rows):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


def print_position_guide():
    guide = [str(i + 1) for i in range(9)]
    rows = [guide[i:i + 3] for i in range(0, 9, 3)]
    print("Positions:")
    for i, row in enumerate(rows):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  
    (0, 4, 8), (2, 4, 6),             
]


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]


def minimax(board, depth, is_maximizing):
    win = winner(board)
    if win == AI:
        return 10 - depth
    if win == HUMAN:
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(best_score, score)
        return best_score


def best_ai_move(board):
    moves = available_moves(board)

    if len(moves) == 9:
        return random.choice(moves)

    best_score = -math.inf
    best_move = moves[0]
    for move in moves:
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def get_human_move(board):
    while True:
        raw = input("Your move (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number between 1 and 9.")
            continue
        pos = int(raw) - 1
        if pos < 0 or pos > 8:
            print("Please enter a number between 1 and 9.")
            continue
        if board[pos] != EMPTY:
            print("That spot is taken. Try again.")
            continue
        return pos


def choose_who_goes_first():
    while True:
        choice = input("Do you want to go first? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please answer y or n.")


def play_round():
    board = new_board()
    human_turn = choose_who_goes_first()

    print_position_guide()
    print_board(board)

    while True:
        if human_turn:
            pos = get_human_move(board)
            board[pos] = HUMAN
        else:
            print("AI is thinking...")
            pos = best_ai_move(board)
            board[pos] = AI

        print_board(board)

        win = winner(board)
        if win == HUMAN:
            print("You win! 🎉")
            return
        if win == AI:
            print("AI wins! 🤖")
            return
        if is_full(board):
            print("It's a draw!")
            return

        human_turn = not human_turn


def main():
    print("=" * 40)
    print("       TIC-TAC-TOE  (vs. unbeatable AI)")
    print("=" * 40)

    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()