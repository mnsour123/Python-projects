import random
import time

OPERATORS = ['+', '-', '*', '/']
TOTAL_PROBLEMS = 10

DIFFICULTIES = {
    '1': ('Easy', 3, 10),
    '2': ('Medium', 3, 12),
    '3': ('Hard', 5, 20),
}


def choose_difficulty():
    print('Choose a difficulty:')
    for key, (name, lo, hi) in DIFFICULTIES.items():
        print(f'  {key}) {name}  (operands {lo}-{hi})')
    while True:
        choice = input('> ').strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print('Please enter 1, 2, or 3.')


def generate_problem(min_operand, max_operand):
    operator = random.choice(OPERATORS)

    if operator == '/':
        right = random.randint(min_operand, max_operand)
        answer = random.randint(min_operand, max_operand)
        left = right * answer
        expr = f'{left} / {right}'
        return expr, answer

    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)

    if operator == '-':
        left, right = max(left, right), min(left, right)

    expr = f'{left} {operator} {right}'
    answer = eval(expr)
    return expr, answer


def ask_problem(number, expr, answer):
    """Ask a single problem until answered correctly. Returns wrong-attempt count."""
    wrong_attempts = 0
    while True:
        guess = input(f'Problem #{number}: {expr} = ').strip()

        if guess.lower() == 'q':
            print('Quitting quiz early. See you next time!')
            raise SystemExit

        try:
            guess_value = float(guess)
        except ValueError:
            print("  That doesn't look like a number, try again.")
            continue

        if guess_value == answer:
            return wrong_attempts

        wrong_attempts += 1
        print('  Not quite, try again.')


def run_quiz():
    name, min_operand, max_operand = choose_difficulty()
    wrong = 0
    first_try_correct = 0

    input(f'\n{name} mode selected. Press enter to start (or type "q" during the quiz to quit) ')
    print('---------------------')
    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem(min_operand, max_operand)
        attempts_wrong = ask_problem(i + 1, expr, answer)
        wrong += attempts_wrong
        if attempts_wrong == 0:
            first_try_correct += 1

    end_time = time.time()
    total_time = round(end_time - start_time)
    accuracy = round(100 * first_try_correct / TOTAL_PROBLEMS)

    print('---------------------')
    print(f'Nice work! You finished in {total_time} seconds')
    print(f'Wrong guesses: {wrong}')
    print(f'First-try accuracy: {accuracy}% ({first_try_correct}/{TOTAL_PROBLEMS})')
    print(f'Average time per problem: {round(total_time / TOTAL_PROBLEMS, 1)}s')


if __name__ == '__main__':
    try:
        run_quiz()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        print('\nQuiz interrupted. Bye!')
