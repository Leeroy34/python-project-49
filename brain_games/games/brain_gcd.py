import prompt
import random
from brain_games.scripts.greet import greet


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def main():
    name = greet()
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f'Question: {number1} {number2} ')

        answer = gcd(number1, number2)
        user_answer = prompt.string('Your answer: ')

        if int(user_answer) == answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was {answer}")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
