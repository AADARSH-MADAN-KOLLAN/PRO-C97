import random

print("✧･ﾟ: *✧･ﾟ:* WELCOME TO THE NUMBER GUESSING GAME! *:･ﾟ✧*:･ﾟ✧ \n")
print("Guess a number from 1 to 10! You have 5 chances!\n")
number = random.randrange(1,10)
chance=0

while chance<5:
    guess = int(input("Your Guess : "))
    if guess == number:
        print("CONGRATULATIONS YOU WIN!!!!")
        break
    elif guess<number:
        chance+=1
        print(f"Sorry, your guess is wrong. You have {5-chance} chances left! HINT: It's a bigger number!")
    elif guess>number:
        chance+=1
        print(f"Sorry, your guess is wrong. You have {5-chance} chances left! HINT: It's a smaller number!")
    else:
        chance+=1
        print(f"Sorry, your guess is wrong. You have {5-chance} chances left!")