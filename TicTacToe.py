################################################################################
## Tic Tac Toe
# Date: February 13, 2017
# Author: Sherman Chow
#
## Features:
# Player vs player (player chooses positions based on keyboard"s keypad)
# Player vs AI (alpha-beta pruning)
# Player (X) goes first, AI (O) goes second
################################################################################

# from Tkinter import *

# root = Tk()
# root.title("Tic Tac Toe")
# root.geometry("300x300")
# root.mainloop()

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

# function to find all legal moves in current state of game board
def findLegalMoves(thisBoard):
    legalMoves = [None]
    for i, val in enumerate(thisBoard):
        if val == " ":
            legalMoves.append(i)
    return legalMoves

# function to evaluate the score of a move
def evaluate(thisBoard):
    bestScore = 0;
    currBoard = list(thisBoard)
    # evaluate score for each of the 8 lines (3 rows, 3 columns, 2 diagonals)
    bestScore += evaluateScore(currBoard, 1, 2, 3)   # row 1
    bestScore += evaluateScore(currBoard, 4, 5, 6)   # row 2
    bestScore += evaluateScore(currBoard, 7, 8, 9)   # row 3
    bestScore += evaluateScore(currBoard, 1, 4, 7)   # col 1
    bestScore += evaluateScore(currBoard, 2, 5, 8)   # col 2
    bestScore += evaluateScore(currBoard, 3, 6, 9)   # col 3
    bestScore += evaluateScore(currBoard, 1, 5, 9)   # diagonal 1
    bestScore += evaluateScore(currBoard, 3, 5, 7)   # diagonal 2
    return bestScore

def evaluateScore(thisBoard, cell_1, cell_2, cell_3):
    bestScore = 0

    # first cell
    if thisBoard[cell_1] == "O":    # if cell_1 is AI
        bestScore = 1
    elif thisBoard[cell_1] == "X":  # if cell_1 is user
        bestScore = -1

    # second cell
    if thisBoard[cell_2] == "O":    # if cell_2 is AI
        if bestScore == 1:                  # if cell_1 is AI
            bestScore = 10
        elif bestScore == -1:               # if cell_1 is user
            return 0
        else:                               # if cell_1 is empty
            bestScore = 1
    elif thisBoard[cell_2] == "X":  # if cell_2 is user
        if bestScore == -1:                 # if cell_1 is user
            bestScore = -10
        elif bestScore == 1:                # if cell_1 is AI
            return 0
        else:                               # if cell_1 is empty
            bestScore = -1

    # third cell
    if thisBoard[cell_3] == "O":    # if cell_3 is AI
        if bestScore > 0:                   # if cell_1 and/or cell_2 is AI
            bestScore *= 10
        elif bestScore < 0:                 # if cell_1 and/or cell_2 is user
            return 0
        else:                               # if cell_1 and cell_2 are empty
            bestScore = 1
    elif thisBoard[cell_3] == "X":  # if cell_3 is user
        if bestScore < 0:                   # if cell_1 and/or cell_2 is user
            bestScore *= 10
        elif bestScore < 0:                 # if cell_1 and/or cell_2 is AI
            return 0
        else:                               # cell_1 and cell_2 are empty
            bestScore = -1

    return bestScore

# function for minimax AI
def minimax(thisBoard, player, depth):
    newBoard = list(thisBoard)
    legalMoves = findLegalMoves(newBoard)
    del legalMoves[0]   # delete first index. This is because it is None since we start the positions of the cells at index 1

    # initialize and set necessary variables
    bestScore = 0
    mark = ""
    if player == "AI":
        bestScore = float("-inf")
        mark = "O"
    else:
        bestScore = float("inf")
        mark = "X"
    currentScore = 0
    bestMove = -1

    # if the game is over or the depth is reached
    if not legalMoves or depth == 0:
        bestScore = evaluate(newBoard)
    else:
        # iterate through all possible legal moves
        for move in legalMoves:
            # simulate the move in the game board
            newBoard[move] = mark

            # maximizer
            if player == "AI":
                currentScore = minimax(newBoard, "user", depth-1)[0]
                if currentScore > bestScore:
                    bestScore = currentScore
                    bestMove = move
            # minimizer
            else:
                currentScore = minimax(newBoard, "AI", depth-1)[0]
                if currentScore < bestScore:
                    bestScore = currentScore
                    bestMove = move
            # undo the move and revert back to original state of game board
            newBoard[move] = " "
    return (bestScore, bestMove)

# ----------------------------------------------------------------------------------------------------------------------------------
# MAIN
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
# player (X) goes first, AI (O) goes second
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
            # call minimax AI function; minimax(thisBoard, player, depth)
            AI_move = minimax(board, "AI", 3)[1]    # index 0 is the score, index 1 is the move
            # make the best AI move
            board[AI_move] = "O"
            turn += 1

            