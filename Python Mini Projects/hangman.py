import random

def hangman():
    
    word = random.choice(["IronMan", "CaptainAmerica", "Hulk", "Thor", "BlackPanther", "BlackWidow", "AntMan", "CaptainMarvel", "Wanda", "Vision", "Avengers"])

    validLetters_small = 'abcdefghijklmnopqrstuvwxyz' 
    validLetters_big =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turns = 10
    guessmade = ''

 
    while len(word) > 0:
        main = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You Win!!")
            break
        print("Guess the Avenger", main)
        guess = input()

        if guess in validLetters_small or validLetters_big:
            guessmade = guessmade + guess
        else:
            print("Enter a Valid Character")
            guess = input()

        
        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 turns left")
                print("  --------  ")

            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("      O     ")

            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("      O     ")
                print("      |     ")

            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("      O     ")
                print("      |     ")
                print("     /      ")

            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("      O     ")
                print("      |     ")
                print("     / \    ")

            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("    \ O     ")
                print("      |     ")
                print("     / \    ")

            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("    \ O /   ")
                print("      |     ")
                print("     / \    ")

            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("    \ O /|  ")
                print("      |     ")
                print("     / \    ")

            if turns == 1:
                print("1 turns left")
                print("Last chance to save him")
                print("  --------  ")
                print("    \ O_|/  ")
                print("      |     ")
                print("     / \    ")

            if turns == 0:
                print("You Loose")
                print("You let a kind man die")
                print("  --------  ")
                print("    \ O_|   ")
                print("            ")
                print("     / \    ")
                break


name = input("Enter your Name:\n")

print(f"Welocome {name}. Let's start the Game")
print("Guess the names of your Favourite Avengers Characters: ")
print("---"*15)
print("Try to guess the word in less than 10 try")

hangman()

