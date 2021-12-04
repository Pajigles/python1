##PJ Frost
##Programming Assignment 2
##09/14/2021
##SEC.207

def three_things():
    print("Enter your name:")
    name = input()
    print(name)
    print()

    print("Enter a number:")
    number = input()
    number = float(number)
    number = number * number
    print(number)
    print()

    print("Enter a word to have letters counted:")
    words = input()
    print(len(words))

three_things()