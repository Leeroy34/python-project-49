import prompt
import random
from brain_games.scripts.greet import greet


def main():
    name = greet()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')

        if (number % 2 == 0 and user_answer.lower() == 'yes') or \
           (number % 2 != 0 and user_answer.lower() == 'no'):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{'yes' if number % 2 == 0 else 'no'}'.")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
