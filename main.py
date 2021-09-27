##PJ Frost
##Programming Assignment 3
##09/26/2021
##SEC.207
import random

choice = input("Press 1 for Coin Flip or 2 for Art: ")
choice = int(choice)

if (choice == 1):
    def coin_flip():
        number = input("1 or 0? ")
        number = int(number)
        coin = random.randint(0,1)
        if (coin == number):
            print("You win!")
        else:
            print("You lose!")


    coin_flip()

if (choice == 2):
    def art():
        array = [[' ', '_', ' ', ' ', '_', ' '],
                 ['|', '^', '|', '|', '^', '|'],
                 ['|', ' ', '|', '|', ' ', '|'],
                 [' ', '-', ' ', ' ', '-', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 ['|', ' ', ' ', ' ', ' ', '|'],
                 ['|', ' ', ' ', ' ', ' ', '|'],
                 [' ', '|', ' ', ' ', '|', ' '],
                 [' ', ' ', '-', '-', ' ', ' ']]

        for art1 in array:
            for art2 in art1:
                print(art2, end=" ")
            print()


    art()

