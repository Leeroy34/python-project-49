import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    for i in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        operations = ['+', '-', '*']
        operation = random.choice(operations)
        print('What is the result of the expression?')
        print(f"Question: {num1} {operation} {num2}")
        user_answer = prompt.string('Your answer: ')

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        else:
            answer = num1 * num2

        if int(user_answer) == answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was {answer}")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
