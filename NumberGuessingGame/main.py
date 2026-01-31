#This is a Number Guessing Game - runs through CLI
import random
print("Welcome to Guess the number game")
secret_num = random.randint(1,10)
while True: 
    number = int(input("Guess the Number(1-10): "))
    if number==secret_num:
        print("You guessed it right!")
        break
    elif number > secret_num:
        print("Number too high!")
    else:
        print("Number too low!")
print("Thanks for playing!")