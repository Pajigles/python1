##PJ Frost
##Programming Assignment 6 Strings1
##10/29/2021
##SEC.207
import random

actual_board = [[1, 2, 3],
                [4, 'X', 6],
                [7, 8, 9]]

def display_board(): #Displaying the board with updated values

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(actual_board[0][0]) + "   |   " + str(actual_board[0][1]) + "   |   " + str(actual_board[0][2]) +"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(actual_board[1][0]) + "   |   " + 'X' + "   |   " + str(actual_board[1][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(actual_board[2][0]) + "   |   " + str(actual_board[2][1]) + "   |   " + str(actual_board[2][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(actual_board): #Player enters move here

    print("This is your " + str(move_count) + "'st move")  # Player move
    while True:
        player_input = int(input("Enter your move: "))
        for x in range(0, 3):
            for y in range(0, 3):
                if player_input == actual_board[x][y] and actual_board[x][y] != 'O' and actual_board[x][y] != 'X':
                    actual_board[x][y] = 'O'
                    return


def victory_for(actual_board, sign): #Checking victory conditions

        if actual_board[0][0] == actual_board[0][1] == actual_board[0][2]:
            print("Across the top victory!")
            exit()
            return
        elif actual_board[1][0] == actual_board[1][1] == actual_board[1][2] == sign:
            print("Across the middle victory!")
            exit()
            return
        elif actual_board[2][0] == actual_board[2][1] == actual_board[2][2] == sign:
            print("Across the bottom victory!")
            exit()
            return
        elif actual_board[0][0] == actual_board[1][0] == actual_board[2][0] == sign:
            print("Down the left side victory!")
            exit()
            return
        elif actual_board[0][1] == actual_board[1][1] == actual_board[2][1] == sign:
            print("Down the middle victory!")
            exit()
            return
        elif actual_board[0][2] == actual_board[1][2] == actual_board[2][2] == sign:
            print("Down the right side victory!")
            exit()
            return
        elif actual_board[0][0] == actual_board[1][1] == actual_board[2][2] == sign:
            print("Diagonal victory!")
            exit()
            return
        elif actual_board[0][2] == actual_board[1][1] == actual_board[2][0] == sign:
            print("Diagonal victory!")
            exit()
            return


def draw_move(actual_board): #AI makes move here

    while True:
        ai_input = int(random.randrange(1, 10))  # AI move
        for x in range(0, 3):
            for y in range(0, 3):
                 if ai_input == actual_board[x][y] and actual_board[x][y] != 'O' and actual_board[x][y] != 'X':
                    actual_board[x][y] = 'X'
                    return


#main method down here kind of

move_count = 1

while True:
    display_board()
    enter_move(actual_board)
    display_board()
    draw_move(actual_board)


    if move_count >= 2:
        victory_for(actual_board, 'O')
        victory_for(actual_board, 'X')
    if move_count == 4:
        print("It's a tie!")
        exit()
    move_count += 1
