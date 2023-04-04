import prompt
import random
from brain_games.scripts.greet import greet


def main():
    name = greet()
    print('What number is missing in the progression?')
    for i in range(3):
        progression = []
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 10)
        number3 = random.randint(1, 10)

        progression.append(number1)
        for i in range(10):
            number1 += number2
            progression.append(number1)

        answer = progression[number3]
        progression[number3] = '..'

        print(progression)
        user_answer = prompt.string('Your answer: ')

        if int(user_answer) == answer:
            print('Correct!')
        else:
            print(f"""'{user_answer}' is wrong answer ;(.
            Correct answer was {answer}""")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
