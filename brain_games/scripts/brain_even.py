import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if (number % 2 == 0 and answer.lower() == 'yes') or \
           (number % 2 != 0 and answer.lower() == 'no'):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{'yes' if number % 2 == 0 else 'no'}'.")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
