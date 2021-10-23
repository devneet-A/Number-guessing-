import random 
print("Number Guessing Game")

number = random.randint(1, 9)

chances = 0

print("guess a number (between 1 and 9):")

while chances>5:
    guess = int(input("enter your guess:-"))

    if guess==number:
        print("Congratulation YOU won!!!")
        break

    elif guess<number:
        print("Your Guess was too low")

    else:
        print("your guess was wrong")

    chance+=1

if not chances<5:
    print("You Lose!! the number is", number)