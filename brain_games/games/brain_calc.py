import prompt
import random
from brain_games.scripts.greet import greet


def main():
    name = greet()

    for i in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        operations = ['+', '-', '*']
        operation = random.choice(operations)
        print('What is the result of the expression?')
        print(f"Question: {num1} {operation} {num2}")
        reply = prompt.string('Your answer: ')

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        else:
            answer = num1 * num2

        if int(reply) == answer:
            print('Correct!')
        else:
            print(
                f"'{reply}' is wrong answer ;(. Correct answer was '{answer}'"
            )
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
