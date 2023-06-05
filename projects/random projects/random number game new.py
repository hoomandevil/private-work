import random


def lifes():
    return life - 1


number = random.choice(range(101))
level_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level_mode == "hard":
    life = 5
else:
    life = 10

while True:
    print(f"You have {life} attempts goodluck ")
    guess = int(input("Make a Guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        quit()
    elif guess > number:
        print(f"Too high.")
        life -= 1
    else:
        print(f"Too low.")
        life -= 1
    if life == 0:
        print("You lost!!")
        quit()