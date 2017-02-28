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

def check3row_AI(board, mark):
    # horizontals
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return 100
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return 100
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return 100
    # verticals
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return 100
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return 100
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return 100
    # diagonals
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return 100
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return 100
    else:
        return 0

def check3row_opponent(board, mark):
    # horizontals
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return -100
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return -100
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return -100
    # verticals
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return -100
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return -100
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return -100
    # diagonals
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return -100
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return -100
    else:
        return 0

def check2row_AI(board, mark):   # 2-in-a-row (1 empty cell)
    if board[7] == mark and board[5] == mark and board[3] == " ":
        return 10
    elif board[8] == mark and board[5] == mark and board[2] == " ":
        return 10
    elif board[9] == mark and board[5] == mark and board[1] == " ":
        return 10
    elif board[6] == mark and board[5] == mark and board[4] == " ":
        return 10
    elif board[3] == mark and board[5] == mark and board[7] == " ":
        return 10
    elif board[2] == mark and board[5] == mark and board[8] == " ":
        return 10
    elif board[1] == mark and board[5] == mark and board[9] == " ":
        return 10
    elif board[4] == mark and board[5] == mark and board[6] == " ":
        return 10
    elif board[7] == mark and board[8] == mark and board[9] == " ":
        return 10
    elif board[7] == mark and board[4] == mark and board[1] == " ":
        return 10
    elif board[9] == mark and board[8] == mark and board[7] == " ":
        return 10
    elif board[9] == mark and board[6] == mark and board[3] == " ":
        return 10
    elif board[3] == mark and board[6] == mark and board[7] == " ":
        return 10
    elif board[3] == mark and board[2] == mark and board[1] == " ":
        return 10
    elif board[1] == mark and board[4] == mark and board[7] == " ":
        return 10
    else:
        return 0

def check2row_opponent(board, mark):
    if board[7] == mark and board[5] == mark and board[3] == " ":
        return -10
    elif board[8] == mark and board[5] == mark and board[2] == " ":
        return -10
    elif board[9] == mark and board[5] == mark and board[1] == " ":
        return -10
    elif board[6] == mark and board[5] == mark and board[4] == " ":
        return -10
    elif board[3] == mark and board[5] == mark and board[7] == " ":
        return -10
    elif board[2] == mark and board[5] == mark and board[8] == " ":
        return -10
    elif board[1] == mark and board[5] == mark and board[9] == " ":
        return -10
    elif board[4] == mark and board[5] == mark and board[6] == " ":
        return -10
    elif board[7] == mark and board[8] == mark and board[9] == " ":
        return -10
    elif board[7] == mark and board[4] == mark and board[1] == " ":
        return -10
    elif board[9] == mark and board[8] == mark and board[7] == " ":
        return -10
    elif board[9] == mark and board[6] == mark and board[3] == " ":
        return -10
    elif board[3] == mark and board[6] == mark and board[7] == " ":
        return -10
    elif board[3] == mark and board[2] == mark and board[1] == " ":
        return -10
    elif board[1] == mark and board[4] == mark and board[7] == " ":
        return -10
    else:
        return 0

def check1row_AI(board, mark):   # 1-in-a-row (2 empty cells)
    if board[7] == mark and board[8] == " " and board[9] == " ":
        return 1
    elif board[7] == mark and board[5] == " " and board[6] == " ":
        return 1
    elif board[7] == mark and board[4] == " " and board[1] == " ":
        return 1

    elif board[8] == mark and board[7] == " " and board[9] == " ":
        return 1
    elif board[8] == mark and board[5] == " " and board[2] == " ":
        return 1

    elif board[9] == mark and board[8] == " " and board[7] == " ":
        return 1
    elif board[9] == mark and board[6] == " " and board[3] == " ":
        return 1
    elif board[9] == mark and board[5] == " " and board[1] == " ":
        return 1

    elif board[4] == mark and board[5] == " " and board[6] == " ":
        return 1
    elif board[4] == mark and board[7] == " " and board[1] == " ":
        return 1

    elif board[5] == mark and board[7] == " " and board[3] == " ":
        return 1
    elif board[5] == mark and board[9] == " " and board[1] == " ":
        return 1
    elif board[5] == mark and board[4] == " " and board[6] == " ":
        return 1
    elif board[5] == mark and board[8] == " " and board[2] == " ":
        return 1

    elif board[6] == mark and board[5] == " " and board[4] == " ":
        return 1
    elif board[6] == mark and board[9] == " " and board[3] == " ":
        return 1

    elif board[1] == mark and board[4] == " " and board[7] == " ":
        return 1
    elif board[1] == mark and board[5] == " " and board[9] == " ":
        return 1
    elif board[1] == mark and board[2] == " " and board[3] == " ":
        return 1

    elif board[2] == mark and board[5] == " " and board[9] == " ":
        return 1
    elif board[2] == mark and board[1] == " " and board[3] == " ":
        return 1

    elif board[3] == mark and board[6] == " " and board[9] == " ":
        return 1
    elif board[3] == mark and board[5] == " " and board[7] == " ":
        return 1
    elif board[3] == mark and board[2] == " " and board[1] == " ":
        return 1
    else:
        return 0

def check1row_opponent(board, mark):
    if board[7] == mark and board[8] == " " and board[9] == " ":
        return -1
    elif board[7] == mark and board[5] == " " and board[6] == " ":
        return -1
    elif board[7] == mark and board[4] == " " and board[1] == " ":
        return -1

    elif board[8] == mark and board[7] == " " and board[9] == " ":
        return -1
    elif board[8] == mark and board[5] == " " and board[2] == " ":
        return -1

    elif board[9] == mark and board[8] == " " and board[7] == " ":
        return -1
    elif board[9] == mark and board[6] == " " and board[3] == " ":
        return -1
    elif board[9] == mark and board[5] == " " and board[1] == " ":
        return -1

    elif board[4] == mark and board[5] == " " and board[6] == " ":
        return -1
    elif board[4] == mark and board[7] == " " and board[1] == " ":
        return -1

    elif board[5] == mark and board[7] == " " and board[3] == " ":
        return -1
    elif board[5] == mark and board[9] == " " and board[1] == " ":
        return -1
    elif board[5] == mark and board[4] == " " and board[6] == " ":
        return -1
    elif board[5] == mark and board[8] == " " and board[2] == " ":
        return -1

    elif board[6] == mark and board[5] == " " and board[4] == " ":
        return -1
    elif board[6] == mark and board[9] == " " and board[3] == " ":
        return -1

    elif board[1] == mark and board[4] == " " and board[7] == " ":
        return -1
    elif board[1] == mark and board[5] == " " and board[9] == " ":
        return -1
    elif board[1] == mark and board[2] == " " and board[3] == " ":
        return -1

    elif board[2] == mark and board[5] == " " and board[9] == " ":
        return -1
    elif board[2] == mark and board[1] == " " and board[3] == " ":
        return -1

    elif board[3] == mark and board[6] == " " and board[9] == " ":
        return -1
    elif board[3] == mark and board[5] == " " and board[7] == " ":
        return -1
    elif board[3] == mark and board[2] == " " and board[1] == " ":
        return -1
    else:
        return 0

# function to evaluate score
def evaluate(thisBoard, player):
    bestScore = 0
    # maximizer
    if player == "AI":
        # print "AI"      # TESTING
        mark = "O"
        score1 = check3row_AI(board, mark)
        # print "score1: ", score1    # TESTING
        score2 = check2row_AI(board, mark)
        # print "score2: ", score2    # TESTING
        score3 = check1row_AI(board, mark)
        # print "score3: ", score3    # TESTING
        if score1 >= score2 and score1 >= score3 and score1 >= bestScore:
            bestScore = score1
        elif score2 >= score1 and score2 >= score3 and score2 >= bestScore:
            bestScore = score2
        elif score3 >= score1 and score3 >= score2 and score3 >= bestScore:
            bestScore = score3
    # minimizer
    else:   # player = "user"
        # print "user"    # TESTING
        mark = "X"
        score1 = check3row_opponent(board, mark)
        # print "score1: ", score1    # TESTING
        score2 = check2row_opponent(board, mark)
        # print "score2: ", score2    # TESTING
        score3 = check1row_opponent(board, mark)
        # print "score3: ", score3    # TESTING
        if score1 <= score2 and score1 <= score3 and score1 <= bestScore:
            bestScore = score1
        elif score2 <= score1 and score2 <= score3 and score2 <= bestScore:
            bestScore = score2
        elif score3 <= score1 and score3 <= score2 and score3 <= bestScore:
            bestScore = score3

    # print "bestScore: ", bestScore     # TESTING
    return bestScore

# function to find all legal moves in current state of game board
def findLegalMoves(thisBoard):
    legalMoves = [None]
    for i, val in enumerate(thisBoard):
        if val == " ":
            legalMoves.append(i)
    return legalMoves

# functiont to simulate a board with possible move
def simulateBoard(thisBoard, move, mark):
    returnBoard = list(thisBoard)
    returnBoard[move] = mark
    return returnBoard

# minimax AI function
# def minimax(thisBoard, player, depth):
#     newBoard = list(thisBoard)
#     if depth == 0:
#         return evaluate(newBoard, player)
#     # maximizer
#     if player == "AI":
#         bestScore = float("-inf")
#         # find all legal moves
#         legalMoves = findLegalMoves(newBoard)
#         # iterate through all legal moves
#         for move in legalMoves:
#             if move != None:
#                 # simulate move in board
#                 simBoard = simulateBoard(newBoard, move, "O")
#                 # resetBoard(simBoard)    # TESTING
#                 # evaluate score of simulated move
#                 score = minimax(simBoard, "user", depth-1)
#                 if score > bestScore:
#                     bestScore = score
#         return bestScore
#     # minimizer
#     else:
#         bestScore = float("inf")
#         # find all legal
#         legalMoves = findLegalMoves(newBoard)
#         # iterate through all legal moves
#         for move in legalMoves:
#             if move != None:
#                 # simulate move in board
#                 simBoard = simulateBoard(newBoard, move, "X")
#                 # resetBoard(simBoard)    # TESTING
#                 # evaluate score of simulated move
#                 score = minimax(simBoard, "AI", depth-1)
#                 if score < bestScore:
#                     bestScore = score
#         return bestScore

# try to save the best move along with the best score
def minimax(thisBoard, player, depth, move):
    newBoard = list(thisBoard)
    # if depth == 0 or checkWin(newBoard, "X") or checkWin(newBoard, "O") or checkTie(newBoard):
    #     best = (evaluate(newBoard, player), move)
    #     return best
    
    if depth == 0:
        best = (evaluate(newBoard, player), move)
        return best

    # maximizer
    if player == "AI":
        bestScore = (float("-inf"), 0)
        # find all legal moves
        legalMoves = findLegalMoves(newBoard)
        # remove None in index 0
        del legalMoves[0]
        # print "AI legal moves: ", legalMoves
        # iterate through all legal moves
        for move in legalMoves:
            # print "move: ", move
            # simulate move in board
            simBoard = simulateBoard(newBoard, move, "O")
            # print "AI POSSIBLE MOVE BOARD"    # TESTING
            # resetBoard(simBoard)    # TESTING
            # evaluate score of simulated move
            score = minimax(simBoard, "user", depth-1, move)
            # print score     # TESTING
            if score[0] > bestScore[0]:
                bestScore = score
        return bestScore
    # minimizer
    else:
        bestScore = (float("inf"), 0)
        # find all legal
        legalMoves = findLegalMoves(newBoard)
        # remove None in index 0
        del legalMoves[0]
        print "user legal moves: ", legalMoves
        # iterate through all legal moves
        for move in legalMoves:
            print "move: ", move
            # simulate move in board
            simBoard = simulateBoard(newBoard, move, "X")
            print "USER POSSIBLE MOVE BOARD"    # TESTING
            resetBoard(simBoard)    # TESTING
            # evaluate score of simulated move
            score = minimax(simBoard, "AI", depth-1, move)
            # print score     # TESTING
            if score[0] < bestScore[0]:
                bestScore = score
                print "user bestScore: ", bestScore
        return bestScore

def AI_bestMove(thisBoard, player, depth, move):
    localBoard = list(thisBoard)
    bestMove = minimax(localBoard, player, depth, move)[1]
    return bestMove
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

            # make AI move
            # -----------------------------------------
            # minimax(thisBoard, player, depth)
            # minimax(board, "AI", 3)
            # print AI_bestMove(board, "AI", 3)
            board[AI_bestMove(board, "AI", 3, 0)] = "O";


            # -----------------------------------------

            turn += 1










