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

    print("Player " + player + " turn")
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
def checkWin(board):
    # check if player 1 (X) has won
    # horizontals
    if board[7] == "X" and board[8] == "X" and board[9] == "X":
        print("Player 1 wins!")
        return True
    elif board[4] == "X" and board[5] == "X" and board[6] == "X":
        print("Player 1 wins!")
        return True
    elif board[1] == "X" and board[2] == "X" and board[3] == "X":
        print("Player 1 wins!")
        return True
    # verticals
    elif board[7] == "X" and board[4] == "X" and board[1] == "X":
        print("Player 1 wins!")
        return True
    elif board[8] == "X" and board[5] == "X" and board[2] == "X":
        print("Player 1 wins!")
        return True
    elif board[9] == "X" and board[6] == "X" and board[3] == "X":
        print("Player 1 wins!")
        return True
    # diagonals
    elif board[7] == "X" and board[5] == "X" and board[3] == "X":
        print("Player 1 wins!")
        return True
    elif board[1] == "X" and board[5] == "X" and board[9] == "X":
        print("Player 1 wins!")
        return True
    # check if player 2 (O) has won
    # horizontals
    if board[7] == "O" and board[8] == "O" and board[9] == "O":
        print("Player 2 wins!")
        return True
    elif board[4] == "O" and board[5] == "O" and board[6] == "O":
        print("Player 2 wins!")
        return True
    elif board[1] == "O" and board[2] == "O" and board[3] == "O":
        print("Player 2 wins!")
        return True
    # verticals
    elif board[7] == "O" and board[4] == "O" and board[1] == "O":
        print("Player 2 wins!")
        return True
    elif board[8] == "O" and board[5] == "O" and board[2] == "O":
        print("Player 2 wins!")
        return True
    elif board[9] == "O" and board[6] == "O" and board[3] == "O":
        print("Player 2 wins!")
        return True
    # diagonals
    elif board[7] == "O" and board[5] == "O" and board[3] == "O":
        print("Player 2 wins!")
        return True
    elif board[1] == "O" and board[5] == "O" and board[9] == "O":
        print("Player 2 wins!")
        return True
    # no one has won
    else:
        return False


# function for AI
# alpha-beta pruning minimax
# http://catarak.github.io/blog/2015/01/07/solving-tic-tac-toe/

# ---------------------------------------------------------------------------
# initial settings for game board
turn = 0
board = [" "] * 10

# prompt user to select player vs player OR player vs AI
gameType = raw_input("Enter '1' for Player VS Player, Enter '2' for Player VS AI: ")

if gameType == "1":
    while True:
        if checkWin(board) == True:     # continue game if no one has won yet. Otherwise, end game
            break

        if checkTie(board) == True:     # check if a tie has occured
            print("Tie game!")
            break
        
        resetBoard(board)               # reset the game board
        placeTurn(board)                # prompt and place user's mark onto game board
        turn += 1                       # incrememt the turn count

        

    # Display final state of game board
    resetBoard(board)
else:
    print("Do you want to go first [Y/n]?")
    playTurn = raw_input()
    print("IMPLEMENT AI")









