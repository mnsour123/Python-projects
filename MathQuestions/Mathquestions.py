import random
import time
import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

DIFFICULTIES = {
    '1': ('Easy', 3, 10),
    '2': ('Medium', 3, 12),
    '3': ('Hard', 5, 20),
}

DEFAULT_PROBLEM_COUNT = 10


def choose_difficulty():
    print('Choose a difficulty:')
    for key, (name, lo, hi) in DIFFICULTIES.items():
        print(f'  {key}) {name}  (operands {lo}-{hi})')
    while True:
        choice = input('> ').strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print('Please enter 1, 2, or 3.')


def choose_problem_count():
    while True:
        raw = input(f'How many problems? (default {DEFAULT_PROBLEM_COUNT}) > ').strip()
        if raw == '':
            return DEFAULT_PROBLEM_COUNT
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print('Please enter a positive whole number.')


def generate_problem(min_operand, max_operand):
    op_symbol = random.choice(list(OPERATORS))

    if op_symbol == '/':
        # Build a division problem that divides evenly.
        right = random.randint(min_operand, max_operand)
        answer = random.randint(min_operand, max_operand)
        left = right * answer
    else:
        left = random.randint(min_operand, max_operand)
        right = random.randint(min_operand, max_operand)
        if op_symbol == '-':
            # Avoid negative results for a gentler difficulty curve.
            left, right = max(left, right), min(left, right)

    expr = f'{left} {op_symbol} {right}'
    answer = OPERATORS[op_symbol](left, right)
    return expr, answer, op_symbol


def is_correct(guess_value, answer):
    return abs(guess_value - answer) < 1e-9


def ask_problem(number, total, expr, answer):
    """Ask a single problem until answered correctly.
    Returns the number of wrong attempts before getting it right."""
    wrong_attempts = 0
    while True:
        guess = input(f'Problem #{number}/{total}: {expr} = ').strip()
        if guess.lower() == 'q':
            print('Quitting quiz early. See you next time!')
            raise SystemExit
        try:
            guess_value = float(guess)
        except ValueError:
            print("  That doesn't look like a number, try again.")
            continue
        if is_correct(guess_value, answer):
            if wrong_attempts == 0:
                print('  Correct! 🎉')
            else:
                print('  Correct!')
            return wrong_attempts
        wrong_attempts += 1
        print('  Not quite, try again.')


def format_duration(seconds):
    minutes, secs = divmod(round(seconds), 60)
    if minutes:
        return f'{minutes}m {secs}s'
    return f'{secs}s'


def run_quiz():
    name, min_operand, max_operand = choose_difficulty()
    total_problems = choose_problem_count()

    wrong = 0
    first_try_correct = 0
    op_stats = {op: {'seen': 0, 'first_try': 0} for op in OPERATORS}
    best_streak = 0
    current_streak = 0

    input(
        f'\n{name} mode selected, {total_problems} problems. '
        'Press enter to start (or type "q" during the quiz to quit) '
    )
    print('---------------------')
    start_time = time.time()

    for i in range(total_problems):
        expr, answer, op_symbol = generate_problem(min_operand, max_operand)
        attempts_wrong = ask_problem(i + 1, total_problems, expr, answer)

        wrong += attempts_wrong
        op_stats[op_symbol]['seen'] += 1

        if attempts_wrong == 0:
            first_try_correct += 1
            op_stats[op_symbol]['first_try'] += 1
            current_streak += 1
            best_streak = max(best_streak, current_streak)
        else:
            current_streak = 0

    end_time = time.time()
    total_time = end_time - start_time
    accuracy = round(100 * first_try_correct / total_problems)

    print('---------------------')
    print(f'Nice work! You finished in {format_duration(total_time)}')
    print(f'Wrong guesses: {wrong}')
    print(f'First-try accuracy: {accuracy}% ({first_try_correct}/{total_problems})')
    print(f'Average time per problem: {round(total_time / total_problems, 1)}s')
    print(f'Best streak: {best_streak} in a row')

    print('\nBreakdown by operator:')
    for op_symbol, stats in op_stats.items():
        seen = stats['seen']
        if seen == 0:
            continue
        pct = round(100 * stats['first_try'] / seen)
        print(f'  {op_symbol}   {stats["first_try"]}/{seen} first-try ({pct}%)')


def play_again():
    while True:
        choice = input('\nPlay again? (y/n) > ').strip().lower()
        if choice in ('y', 'yes'):
            return True
        if choice in ('n', 'no'):
            return False
        print('Please enter y or n.')


def main():
    while True:
        try:
            run_quiz()
        except SystemExit:
            break
        except KeyboardInterrupt:
            print('\nQuiz interrupted. Bye!')
            break

        if not play_again():
            print('Thanks for playing!')
            break


if __name__ == '__main__':
    main()
