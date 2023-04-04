import prompt
import random
from brain_games.scripts.greet import greet


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

def main():
    name = greet()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        number = random.randint(1, 100)
        if number <= 1:
            answer = 'no'
        else:
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    answer = 'no'
                    break
            else:
                answer = 'yes'

        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
        else:
            print(
                f"""'{user_answer}' is wrong answer ;(.Correct answer was '{answer}""")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
