import prompt
import random


def welocome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def main():
    welocome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = random.randint(0, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if number % 2 == 0:
        if answer == 'yes' or answer == 'Yes':
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
    else:
        if answer == 'no' or answer == 'No':
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")


if __name__ == '__main__':
    main()
