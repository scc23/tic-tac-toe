################################################################################
## Tic Tac Toe
# Date: February 13, 2017
# Author: Sherman Chow
#
## Features:
# Player vs player
# Player vs AI (minimax)
# Player (X) goes first, AI (O) goes second
################################################################################

from Tkinter import *
import tkFont
import tkMessageBox
import random

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
# functions for GUI

# message boxes for  player vs player
def player1Win():
    tkMessageBox.showinfo("Game Over", "Player 1 wins!")

def player2Win():
    tkMessageBox.showinfo("Game Over", "Player 2 wins!")

# message boxes player vs AI
def winMessage():
    tkMessageBox.showinfo("Game Over", "You win!")

def loseMessage():
    tkMessageBox.showinfo("Game Over", "You lose!")

def tieMessage():
    tkMessageBox.showinfo("Game Over", "Tie game!")

def updateGUI(thisBoard, mode):
    buttonPlayer.grid_forget()
    buttonAI.grid_forget()
    # check for empty cell
    if thisBoard[1] == " ":
        button1 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(1, mode))
        button1.grid(row=3, column=1)
    if thisBoard[2] == " ":
        button2 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(2, mode))
        button2.grid(row=3, column=2)
    if thisBoard[3] == " ":
        button3 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(3, mode))
        button3.grid(row=3, column=3)
    if thisBoard[4] == " ":
        button4 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(4, mode))
        button4.grid(row=2, column=1)
    if thisBoard[5] == " ":
        button5 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(5, mode))
        button5.grid(row=2, column=2)
    if thisBoard[6] == " ":
        button6 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(6, mode))
        button6.grid(row=2, column=3)
    if thisBoard[7] == " ":
        button7 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(7, mode))
        button7.grid(row=1, column=1)
    if thisBoard[8] == " ":
        button8 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(8, mode))
        button8.grid(row=1, column=2)
    if thisBoard[9] == " ":
        button9 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(9, mode))
        button9.grid(row=1, column=3)

    # check for "X"
    if thisBoard[1] == "X":
        button1 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button1.grid(row=3, column=1)
    if thisBoard[2] == "X":
        button2 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button2.grid(row=3, column=2)
    if thisBoard[3] == "X":
        button3 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button3.grid(row=3, column=3)
    if thisBoard[4] == "X":
        button4 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button4.grid(row=2, column=1)
    if thisBoard[5] == "X":
        button5 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button5.grid(row=2, column=2)
    if thisBoard[6] == "X":
        button6 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button6.grid(row=2, column=3)
    if thisBoard[7] == "X":
        button7 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button7.grid(row=1, column=1)
    if thisBoard[8] == "X":
        button8 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button8.grid(row=1, column=2)
    if thisBoard[9] == "X":
        button9 = Button(root, text="X", state=DISABLED, width=3, height=0, font=customFont)
        button9.grid(row=1, column=3)

    # check for "O"
    if thisBoard[1] == "O":
        button1 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button1.grid(row=3, column=1)
    if thisBoard[2] == "O":
        button2 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button2.grid(row=3, column=2)
    if thisBoard[3] == "O":
        button3 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button3.grid(row=3, column=3)
    if thisBoard[4] == "O":
        button4 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button4.grid(row=2, column=1)
    if thisBoard[5] == "O":
        button5 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button5.grid(row=2, column=2)
    if thisBoard[6] == "O":
        button6 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button6.grid(row=2, column=3)
    if thisBoard[7] == "O":
        button7 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button7.grid(row=1, column=1)
    if thisBoard[8] == "O":
        button8 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button8.grid(row=1, column=2)
    if thisBoard[9] == "O":
        button9 = Button(root, text="O", state=DISABLED, width=3, height=0, font=customFont)
        button9.grid(row=1, column=3)

# ----------------------------------------------------------------------------------------------------------------------------------
# functions for AI

# function to find all legal moves in current state of game board
def findLegalMoves(thisBoard):
    legalMoves = [None]
    for i, val in enumerate(thisBoard):
        if val == " ":
            # add position to list if the cell is empty
            legalMoves.append(i)
    return legalMoves

# function to evaluate the score of a move
def evaluate(thisBoard):
    bestScore = 0;
    currBoard = list(thisBoard)
    # evaluate score for each of the 8 lines (3 rows, 3 columns, 2 diagonals)
    # horizontals
    bestScore += evaluateScore(currBoard, 1, 2, 3)   # row 1
    bestScore += evaluateScore(currBoard, 4, 5, 6)   # row 2
    bestScore += evaluateScore(currBoard, 7, 8, 9)   # row 3
    # verticals
    bestScore += evaluateScore(currBoard, 1, 4, 7)   # col 1
    bestScore += evaluateScore(currBoard, 2, 5, 8)   # col 2
    bestScore += evaluateScore(currBoard, 3, 6, 9)   # col 3
    # digaonals
    bestScore += evaluateScore(currBoard, 1, 5, 9)   # diagonal 1
    bestScore += evaluateScore(currBoard, 3, 5, 7)   # diagonal 2

    return bestScore

# function to evaluate heuristics
    # 3-in-a-row for AI: +100
    # 2-in-a-row for AI: +10
    # 1-in-a-row for AI: +1
    # 3-in-a-row for User: -100
    # 2-in-a-row for User: -10
    # 1-in-a-row for User: -1
    # Otherwise: 0
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
    # find all legal moves and store them in list
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
            # resetBoard(newBoard)                                # TESTING
            # maximizer
            if player == "AI":
                currentScore = minimax(newBoard, "user", depth-1)[0]
                # print "[AI]\tcurrentscore:\t", currentScore     # TESTING
                # print "[user]\tbestScore:\t", bestScore         # TESTING
                if currentScore > bestScore:
                    bestScore = currentScore
                    bestMove = move
            # minimizer
            else:
                currentScore = minimax(newBoard, "AI", depth-1)[0]
                # print "[AI]\tcurrentscore:\t", currentScore     # TESTING
                # print "[user]\tbestScore:\t", bestScore         # TESTING
                if currentScore < bestScore:
                    bestScore = currentScore
                    bestMove = move
            # undo the move and revert back to original state of game board
            newBoard[move] = " "
    return (bestScore, bestMove)

# function for easy mode AI, make a random move
def easyMode(thisBoard):
    # find all possible legal moves
    legalMoves = findLegalMoves(thisBoard)
    del legalMoves[0]   # delete first index. This is because it is None since we start the positions of the cells at index 1
    # print "AI legalMoves: ", legalMoves                         # TESTING
    return random.choice(legalMoves)

# ----------------------------------------------------------------------------------------------------------------------------------
# MAIN
# initial settings for game board
board = [" "] * 10
board[0] = None
global turn
turn = 0

# GUI setup
# -----------------------------------------------------------------------------
root = Tk()
root.title("Tic-Tac-Toe")
# root.geometry("310x310")
w = 310 # width for the Tk root
h = 310 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# minimum size for window
root.minsize(310, 310)

# functions for GUI player vs player game
def updateGUIBoard(pos):
    mark = ""
    xCount = 0
    oCount = 0
    for val in board:
        if val == "X":
            xCount += 1
        elif val == "O":
            oCount += 1
    if oCount < xCount:
        mark = "O"
    else:
        mark = "X"
    board[pos] = mark
    # resetBoard(board)         # TESTING
    updateButton = Button(root, text=mark, state=DISABLED, width=3, height=0, font=customFont)
    if pos == 1:
        updateButton.grid(row=3, column=1)
    elif pos == 2:
        updateButton.grid(row=3, column=2)
    elif pos == 3:
        updateButton.grid(row=3, column=3)
    elif pos == 4:
        updateButton.grid(row=2, column=1)
    elif pos == 5:
        updateButton.grid(row=2, column=2)
    elif pos == 6:
        updateButton.grid(row=2, column=3)
    elif pos == 7:
        updateButton.grid(row=1, column=1)
    elif pos == 8:
        updateButton.grid(row=1, column=2)
    elif pos == 9:
        updateButton.grid(row=1, column=3)

    if checkWin(board, "X"):
        player1Win()
        return
    elif checkWin(board, "O"):
        player2Win()
        return
    elif checkTie(board):
        tieMessage()
        return

def startPlayerGame():
    buttonPlayer.grid_forget()
    buttonAI.grid_forget()
    # setup game board
    if board[1] == " ":
        button1 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(1))
        button1.grid(row=3, column=1)
    if board[2] == " ":
        button2 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(2))
        button2.grid(row=3, column=2)
    if board[3] == " ":
        button3 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(3))
        button3.grid(row=3, column=3)
    if board[4] == " ":
        button4 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(4))
        button4.grid(row=2, column=1)
    if board[5] == " ":
        button5 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(5))
        button5.grid(row=2, column=2)
    if board[6] == " ":
        button6 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(6))
        button6.grid(row=2, column=3)
    if board[7] == " ":
        button7 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(7))
        button7.grid(row=1, column=1)
    if board[8] == " ":
        button8 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(8))
        button8.grid(row=1, column=2)
    if board[9] == " ":
        button9 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard(9))
        button9.grid(row=1, column=3)



# functions for GUI player vs AI game
def updateGUIBoard_AI(pos, mode):
    mark = "X"
    xCount = 0
    oCount = 0
    board[pos] = mark
    # resetBoard(board)         # TESTING
    updateButton = Button(root, text=mark, state=DISABLED, width=3, height=0, font=customFont)
    if pos == 1:
        updateButton.grid(row=3, column=1)
    elif pos == 2:
        updateButton.grid(row=3, column=2)
    elif pos == 3:
        updateButton.grid(row=3, column=3)
    elif pos == 4:
        updateButton.grid(row=2, column=1)
    elif pos == 5:
        updateButton.grid(row=2, column=2)
    elif pos == 6:
        updateButton.grid(row=2, column=3)
    elif pos == 7:
        updateButton.grid(row=1, column=1)
    elif pos == 8:
        updateButton.grid(row=1, column=2)
    elif pos == 9:
        updateButton.grid(row=1, column=3)

    # AI's turn right after player makes a move
    # print "MODE: ", mode
    if mode == 1:
        AI_move = easyMode(board)
    else:
        AI_move = minimax(board, "AI", mode)[1]
    board[AI_move] = "O"

    # update GUI with AI's move
    updateGUI(board, mode)

    if checkWin(board, "X"):
        winMessage()
        return
    elif checkWin(board, "O"):
        loseMessage()
        return
    elif checkTie(board):
        tieMessage()
        return

def startAIGame(mode):
    easyButton.grid_forget()
    normalButton.grid_forget()
    hardButton.grid_forget()
    # setup game board
    if board[1] == " ":
        button1 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(1, mode))
        button1.grid(row=3, column=1)
    if board[2] == " ":
        button2 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(2, mode))
        button2.grid(row=3, column=2)
    if board[3] == " ":
        button3 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(3, mode))
        button3.grid(row=3, column=3)
    if board[4] == " ":
        button4 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(4, mode))
        button4.grid(row=2, column=1)
    if board[5] == " ":
        button5 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(5, mode))
        button5.grid(row=2, column=2)
    if board[6] == " ":
        button6 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(6, mode))
        button6.grid(row=2, column=3)
    if board[7] == " ":
        button7 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(7, mode))
        button7.grid(row=1, column=1)
    if board[8] == " ":
        button8 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(8, mode))
        button8.grid(row=1, column=2)
    if board[9] == " ":
        button9 = Button(root, text=" ", width=13, height=6, command=lambda:updateGUIBoard_AI(9, mode))
        button9.grid(row=1, column=3)

def selectDifficulty():
    buttonPlayer.grid_forget()
    buttonAI.grid_forget()

    global easyButton
    global normalButton
    global hardButton

    easyButton = Button(root, text="Easy Mode", width=13, height=2, font=menuFont, command=lambda:startAIGame(1))
    normalButton = Button(root, text="Normal Mode", width=13, height=2, font=menuFont, command=lambda:startAIGame(2))
    hardButton = Button(root, text="Hard Mode", width=13, height=2, font=menuFont, command=lambda:startAIGame(3))

    easyButton.grid(row=1, column=1)
    normalButton.grid(row=2, column=1)
    hardButton.grid(row=3, column=1)


# GUI menu
customFont = tkFont.Font(family="Helvetica", size=36, weight=tkFont.BOLD)
menuFont = tkFont.Font(family="Helvetica", size=20)

# display the game menu
buttonPlayer = Button(root, text="Player vs Player", width=15, height=3, font=menuFont, command=lambda:startPlayerGame())
# buttonAI = Button(root, text="Player vs AI", width=15, height=3, font=menuFont, command=lambda:startAIGame())
buttonAI = Button(root, text="Player vs AI", width=15, height=3, font=menuFont, command=lambda:selectDifficulty())

buttonPlayer.grid(row=1, column=1)
buttonAI.grid(row=2, column=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

# keep GUI window open until user closes it
root.mainloop()

## CODE FOR CONSOLE APP
# # -----------------------------------------------------------------------------

# # prompt user to select player vs player OR player vs AI
# print("\nTic-Tac-Toe\n")
# print("Main Menu:")
# print("---------------------")
# print("\n[1] Player VS Player")
# print("\n[2] Player VS AI\n")
# print("---------------------\n")
# gameType = raw_input("Game type: ")
# # invalid input error check
# while gameType != "1" and gameType != "2":
#     print("Invalid input, please try again.")
#     gameType = raw_input("Game type: ")

# # player vs player option
# if gameType == "1":
#     while True:
#         # update board
#         resetBoard(board)
#         updateGUI(board)
#         # check if game over
#         if checkWin(board, "X"):
#             player1Win()
#             print("Player 1 wins!")
#             print("Game over!")
#             break
#         elif checkWin(board, "O"):
#             player2Win()
#             print("Player 2 wins!")
#             print("Game over!")
#             break
#         elif checkTie(board):
#             tieMessage()
#             print("Tie game!")
#             break
        
#         # prompt and place user's mark onto game board
#         placeTurn(board)
#         turn += 1

# # player vs AI option
# # player (X) goes first, AI (O) goes second
# elif gameType == "2":
#     print("\nDifficulty Options:")
#     print("---------------------")
#     print("\n[1] Easy")
#     print("\n[2] Normal")
#     print("\n[3] Hard\n")
#     print("---------------------\n")
#     difficulty = raw_input("Difficulty: ")
#     # invalid input error check
#     while difficulty != "1" and difficulty != "2" and difficulty != "3":
#         print("Invalid input, please try again.")
#         gameType = raw_input("Difficulty: ")

#     while True:
#         # update board
#         resetBoard(board)
#         updateGUI(board)
#         # check if game over
#         if checkWin(board, "O"):
#             loseMessage()
#             print("You lose.")
#             print("Game over!")
#             break
#         elif checkWin(board, "X"):
#             winMessage()
#             print("You win.")
#             print("Game over!")
#             break
#         elif checkTie(board):
#             tieMessage()
#             print("Tie game!")
#             break

#         if turn % 2 == 0:   # user's turn
#             # prompt and place user's mark onto game board
#             placeTurn(board)
#             turn += 1
#         else:   # AI's turn
#             print "AI's turn"
            
#             if difficulty == "1":
#                 AI_move = easyMode(board)
#                 # print "easy mode AI move: ", AI_move              # TESTING
#             else:
#                 # call minimax AI function; minimax(thisBoard, player, depth)
#                 AI_move = minimax(board, "AI", int(difficulty))[1]    # index 0 is the score, index 1 is the move
            
#             # make the best AI move
#             board[AI_move] = "O"
#             turn += 1

# # keep GUI window open until user closes it
# root.mainloop()
