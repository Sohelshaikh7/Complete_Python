import random


def dice_stimulator():

    while True:
        print('\n')
        rolling = str(input("press 1 to roll the dice or 0 to exit: "))
        print('\n')

        if rolling == '1':
            number = random.randint(1, 6)

            if number == 1:
                print(" ----- ")
                print("|     |")
                print("|  0  |")
                print("|     |")
                print(" ----- ")
    
            if number == 2:
                print(" ----- ")
                print("| 0   |")
                print("|     |")
                print("|   0 |")
                print(" ----- ")

            if number == 3:
                print(" ----- ")
                print("|     |")
                print("|0 0 0|")
                print("|     |")
                print(" ----- ")

            if number == 4:
                print(" ----- ")
                print("|0   0|")
                print("|     |")
                print("|0   0|")
                print(" ----- ")

            if number == 5:
                print(" ----- ")
                print("|0   0|")
                print("|  0  |")
                print("|0   0|")
                print(" ----- ")

            if number == 6:
                print(" ----- ")
                print("|0 0 0|")
                print("|     |")
                print("|0 0 0|")
                print(" ----- ") 
        
        else:
            print("Ending the game")
            return


dice_stimulator()