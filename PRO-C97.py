import random

print("✧･ﾟ: *✧･ﾟ:* WELCOME TO THE NUMBER GUESSING GAME! *:･ﾟ✧*:･ﾟ✧\n")
print("Guess a number from 1 to 10! You have 5 chances!\n")
number = random.randrange(1, 10)
chance = 5

while chances != 0:
    guess = int(input(f"Your guess: "))
    if guess == number:
        print("CONGRATULATIONS YOU WIN!!!!")
        exit()
    elif guess < number:
        chance -= 1
        print(f"Sorry, your guess is wrong. You have {chance} chances left! HINT: It's a bigger number!")
    elif guess > number:
        chance -= 1
        print(f"Sorry, your guess is wrong. You have {chance} chances left! HINT: It's a smaller number!")
print("Uh oh. You've run out of chances :(")
