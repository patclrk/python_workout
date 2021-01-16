import random

def guessing_game():
    answer = random.randint(1,100)

    while True:
        guess = int(input('Enter a number: '))

        if (guess < answer):
            print(f'{guess} is too low!')
        if (guess > answer):
            print(f'{guess} is too high!')
        if (guess == answer):
            print(f'Cool. {guess} is correct.')
            break

guessing_game()