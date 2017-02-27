################################################################################
## Tic Tac Toe
# Date: February 13, 2017
# Author: Sherman Chow
#
## Features:
# Player vs player (player chooses positions based on keyboard"s keypad)
# Player vs AI (alpha-beta pruning)
# Choice of who goes first (X or O)
################################################################################

import numpy

# function to reset the game board
def resetBoard(board):
    print("___________________")
    print("|     |     |     |")
    print("|  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + "  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  |")
    print("|_____|_____|_____|")
    print("")

# function to place the player's mark onto the game board
def placeTurn(board):
    position    =   0    # value of position (1, 2, 3, 4, 5, 6, 7, 8, 9)
    player      =   0    # player 1 or 2
    mark        =   0    # "X" or "O"

    # determine whose turn it is
    if turn % 2 == 0:
        player  =   "1"
        mark    =   "X"
    else:
        player  =   "2"
        mark    =   "O"

    print("Player " + player + "'s turn")
    position = raw_input("Please enter a position: ")   # prompt user for position

    # user input error check
    while position != "1" and position != "2" and position != "3" and position != "4" and position != "5" and position != "6" and position != "7" and position != "8" and position != "9":
        position = raw_input("Invalid position, please enter a position: ")
    while board[int(position)] != " ":
        position = raw_input("Invalid position, please enter a position: ")

    # place mark on board
    if position == "1":
        board[1] = mark
    elif position == "2":
        board[2] = mark
    elif position == "3":
        board[3] = mark
    elif position == "4":
        board[4] = mark
    elif position == "5":
        board[5] = mark
    elif position == "6":
        board[6] = mark
    elif position == "7":
        board[7] = mark
    elif position == "8":
        board[8] = mark
    elif position == "9":
        board[9] = mark

# function to check if a tie occured
def checkTie(board):
    # check if all positions are filled up
    if board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
        return True
    else:
        return False

# function to check if anyone has won (existance of combination of "X" or "O" in a row)
def checkWin(board, mark):
    # horizontals
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    # verticals
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True
    # diagonals
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    else:
        return False

# ----------------------------------------------------------------------------------------------------------------------------------
# functions for AI
# alpha-beta pruning minimax
# http://catarak.github.io/blog/2015/01/07/solving-tic-tac-toe/






# ---------------------------------------------------------------------------
# initial settings for game board
turn = 0
board = [" "] * 10
board[0] = None

# prompt user to select player vs player OR player vs AI
gameType = raw_input("Enter '1' for Player VS Player, Enter '2' for Player VS AI: ")
while gameType != "1" and gameType != "2":
    gameType = raw_input("Enter '1' for Player VS Player, Enter '2' for Player VS AI: ")

# player vs player option
if gameType == "1":
    while True:
        # update board
        resetBoard(board)

        # check if game over
        if checkWin(board, "X"):
            print("Player 1 wins!")
            print("Game over!")
            break
        elif checkWin(board, "O"):
            print("Player 2 wins!")
            print("Game over!")
        elif checkTie(board):
            print("Tie game!")
            break
        
        # prompt and place user's mark onto game board
        placeTurn(board)
        turn += 1

# player vs AI option
# player goes first, AI goes second
else:
    while True:
        # update board
        resetBoard(board)

        # check if game over
        if checkWin(board, "O"):
            print("You lose.")
            print("Game over!")
            break
        if checkWin(board, "X"):
            print("You win.")
            print("Game over!")
            break
        if checkTie(board):
            print("Tie game!")
            break

        if turn % 2 == 0:   # user's turn
            # prompt and place user's mark onto game board
            placeTurn(board)
            turn += 1
        else:   # AI's turn
            print "AI's turn"



            turn += 1










