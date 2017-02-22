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
        return True
    elif board[4] == "X" and board[5] == "X" and board[6] == "X":
        return True
    elif board[1] == "X" and board[2] == "X" and board[3] == "X":
        return True
    # verticals
    elif board[7] == "X" and board[4] == "X" and board[1] == "X":
        return True
    elif board[8] == "X" and board[5] == "X" and board[2] == "X":
        return True
    elif board[9] == "X" and board[6] == "X" and board[3] == "X":
        return True
    # diagonals
    elif board[7] == "X" and board[5] == "X" and board[3] == "X":
        return True
    elif board[1] == "X" and board[5] == "X" and board[9] == "X":
        return True
    # check if player 2 (O) has won
    # horizontals
    if board[7] == "O" and board[8] == "O" and board[9] == "O":
        return True
    elif board[4] == "O" and board[5] == "O" and board[6] == "O":
        return True
    elif board[1] == "O" and board[2] == "O" and board[3] == "O":
        return True
    # verticals
    elif board[7] == "O" and board[4] == "O" and board[1] == "O":
        return True
    elif board[8] == "O" and board[5] == "O" and board[2] == "O":
        return True
    elif board[9] == "O" and board[6] == "O" and board[3] == "O":
        return True
    # diagonals
    elif board[7] == "O" and board[5] == "O" and board[3] == "O":
        return True
    elif board[1] == "O" and board[5] == "O" and board[9] == "O":
        return True
    # no one has won
    else:
        return False

# function for AI
# alpha-beta pruning minimax
# http://catarak.github.io/blog/2015/01/07/solving-tic-tac-toe/

numberOfPossibleWins = 8
winningPositions = numpy.array( [ [1,2,3],[4,5,6],[7,8,9],[7,4,1],[8,5,2],[9,6,3],[7,5,3],[1,5,9] ] )

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
    # no one has won
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

def row1check_opponent(board, mark):
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

# function to find all legal moves in board
def findLegalMoves(board):
    legalMoves = [None]
    for i, val in enumerate(board):
        if val == " ":
            legalMoves.append(i)
    return legalMoves

# # simulate a board with possible move
# def simulateBoard(board, move, mark):
#     newBoard = board
#     newBoard[move] = mark

def evaluateScore(player, board):
    bestScore = 0
    # maximizer
    if player == "AI":
        mark = "O"
        score1 = check3row_AI(board, mark)
        score2 = check2row_AI(board, mark)
        score3 = check1row_AI(board, mark)
        if score1 >= score2 and score1 >= score3:
            bestScore = score1
        elif score2 >= score1 and score2 >= score3:
            bestScore = score2q
        elif score3 >= score1 and score3 >= score2:
            bestScore = score3
    # minimizer
    else:   # player = "user"
        mark = "X"
        score1 = check3row_opponent(board, mark)
        score2 = check2row_opponent(board, mark)
        score3 = check1row_opponent(board, mark)
        if score1 <= score2 and score1 <= score3:
            bestScore = score1
        elif score2 <= score1 and score2 <= score3:
            bestScore = score2
        elif score3 <= score1 and score3 <= score2:
            bestScore = score3

    return bestScore


def minimax(board, player, alpha, beta, depth):
    if checkWin(board) || checkTie(board) || depth == 0:
        return evaluateScore(board)
    
    legalMoves = findLegalMoves(board)
    # maximizer
    if player == "AI":
        # find max and store in alpha
        bestScore = float("-inf")
        for move in legalMoves:
            score = minimax(board, "user", alpha, beta, depth-1)
            if score > alpha:
                alpha = score
            if alpha >= beta:
                break   # prune
        return alpha
    # minimizer
    else:   # player == "user"
        # find min and store in beta
        bestScore = float("inf")
        for move in legalMoves:
            score = minimax(level-1, computer, alpha, beta)
            if score < beta:
                beta = score
            if alpha >= beta:
                break   # prune
        return beta

# alpha-beta(player,board,alpha,beta)
#     if(game over in current board position)
#         return winner

#     children = all legal moves for player from this board
#     if(max's turn)
#         for each child
#             score = alpha-beta(other player,child,alpha,beta)
#             if score > alpha then alpha = score (we have found a better best move)
#             if alpha >= beta then return alpha (cut off)
#         return alpha (this is our best move)
#     else (min's turn)
#         for each child
#             score = alpha-beta(other player,child,alpha,beta)
#             if score < beta then beta = score (opponent has found a better worse move)
#             if alpha >= beta then return beta (cut off)
#         return beta (this is the opponent's best move)


# ---------------------------------------------------------------------------
# initial settings for game board
turn = 0
board = [" "] * 9
board[0] = None

# prompt user to select player vs player OR player vs AI
gameType = raw_input("Enter '1' for Player VS Player, Enter '2' for Player VS AI: ")
while gameType != "1" and gameType != "2":
    gameType = raw_input("Enter '1' for Player VS Player, Enter '2' for Player VS AI: ")

# player vs player option
if gameType == "1":
    while True:
        # check if game over
        if checkWin(board) == True:
            print("Game over!")
            break
        if checkTie(board) == True:
            print("Tie game!")
            break
        # update board
        resetBoard(board)
        # prompt and place user's mark onto game board
        placeTurn(board)
        turn += 1

    # Display final state of game board
    resetBoard(board)

# player vs AI option
else:
    # print("Do you want to go first [Y/n]?")
    # playTurn = raw_input()
    # while playTurn != "Y" or playTurn != "y" or playTurn != "N" or playTurn != "n":
    #     print("Do you want to go first [Y/n]?")
    #     playTurn = raw_input()
    
    # implement AI

    while True:
        # check if game over
        if checkWin(board) == True:
            print("Game over!")
            break
        if checkTie(board) == True:
            print("Tie game!")
            break

        # update board
        resetBoard(board)

        if turn % 2 == 0:   # user's turn
            # prompt and place user's mark onto game board
            placeTurn(board)
            turn += 1
        else:   # AI's turn
            minimax(board, float("-inf"), float("inf"), 0, 2)
            turn += 1

    # Display final state of game board
    resetBoard(board)










