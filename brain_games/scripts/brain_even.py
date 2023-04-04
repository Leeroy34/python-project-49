import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes' or answer == 'Yes':
                print('Correct!')
            else:
                print(
                    f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}")
                break
        else:
            if answer == 'no' or answer == 'No':
                print('Correct!')
            else:
                print(
                    f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}")
                break
        i += 1

    if i == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
