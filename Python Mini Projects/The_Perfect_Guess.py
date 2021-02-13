import random

randNumber = random.randint(1, 100)
# print(randNumber)

userGuess = None
guesses = 0


while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if (userGuess == randNumber):
        print("You guessed it RIGHT !!")
    else:
        if (userGuess > randNumber):
            print("You guessed it WRONG !! Enter a SMALLER NUMBER")
        else:
            print("You guessed it WRONG !! Enter a LARGER NUMBER")

print(f"You guessed the number in {guesses} guesses")


# with open("high_score.txt", "r") as f:
#     high_score = int(f.read())

# if (guesses < high_score):
#     print("You have just broken the high score !!")
#     with open("high_score.txt", "w") as f:
#         f.write(str(guesses))
