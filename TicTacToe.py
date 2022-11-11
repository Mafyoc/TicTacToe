import random
#enables the random function for the computers move.

"""
Declares global variables, and requests input from the player for their choice of 'x' or 'o'
"""
isDraw = False
playerMoves = 0
computerMoves = 0
boardValues = {"0,0": "_", "1,0": "_", "2,0": "_", "0,1": "_", "1,1": "_", "2,1": "_", "0,2": "_", "1,2": "_", "2,2": "_"}
playerLetter = input("Welcome to Tic-Tac-Toe game, please choose your letter ('x' or 'o')?")

"""
Sets the computer letter based on what letter the player has chosen
"""
if playerLetter == "x":
    computerLetter = "o"
else:
    computerLetter = "x"

"""
player_move function
Gets a reference to the global values of playerMoves and isDraw, checks if all spaces on the board have been filled and 
declares a draw, if there are still spaces left on the board it will ask the player for a coordinate for the next move.
Checks that the entered coordinate is an empty space on the board, as signified by the "_". If the chosen coordinate is 
empty the entry in the dictionary will be updated with the players chosen letter, board is then reprinted, player moves 
is increased by 1, and then runs check_player_win to see if that move makes 3 in a row. If the players entered 
coordinates aren't a blank space or dont match any keys in the dictionary, it will warn the player that their coordinate 
is wrong, and rerun the player move function to request a new input.
"""
def player_move():
    global playerMoves
    global isDraw
    check_for_remaining_spaces()
    if isDraw == True:
        print("DRAW")
    else:
        playerCurrentInput = input("Please enter the coordinates of your next move (x,y)?")
    if boardValues.get(playerCurrentInput) == "_":
        boardValues.update({playerCurrentInput: playerLetter})
        update_board()
        playerMoves += 1
        check_player_win()
    else:
        print("Unfortunately, the (" + playerCurrentInput + ") move you have entered is already used, please enter a new move?")
        player_move()


"""
computer_move function
Gets reference to the number of computer moves. Checks that there are any remaining spaces, if there are none it will 
declare a draw. If there are empty spaces still on the board, the computer will randomly select a key from the 
dictionary of boardvalues until it finds an empty space. Then it will update that dictionary value with the computers 
letter, reprint the board, increase the computers moves by 1 and check if the computer has won.
"""
def computer_move():
    global computerMoves
    check_for_remaining_spaces()
    if isDraw == True:
        print("DRAW")
    else:
        computerCurrentInput = random.choice(list(boardValues.keys()))
        if boardValues.get(computerCurrentInput) == "_":
            boardValues.update({computerCurrentInput: computerLetter})
            print("Computer has chosen: " + computerCurrentInput)
            update_board()
            computerMoves += 1
            check_computer_win()
        else:
            computer_move() #Reruns computer_move until an empty space is found.


"""
checks all possible 3 in a row combinations to see if the player has won.
"""
def check_player_win():
    if boardValues.get("0,0") == playerLetter and boardValues.get("1,0") == playerLetter and boardValues.get("2,0") == playerLetter:
        print("Congratulations! You won in", playerMoves, "moves.")
    elif boardValues.get("0,1") == playerLetter and boardValues.get("1,1") == playerLetter and boardValues.get("2,1") == playerLetter:
        print("Congratulations! You won in", playerMoves, "moves.")
    elif boardValues.get("0,2") == playerLetter and boardValues.get("1,2") == playerLetter and boardValues.get("2,2") == playerLetter:
        print("Congratulations! You won in", playerMoves, "moves.")
    elif boardValues.get("0,0") == playerLetter and boardValues.get("0,1") == playerLetter and boardValues.get("0,2") == playerLetter:
        print("Congratulations! You won in", playerMoves, "moves.")
    elif boardValues.get("1,0") == playerLetter and boardValues.get("1,1") == playerLetter and boardValues.get("1,2") == playerLetter:
        print("Congratulations! You won in", playerMoves, "moves.")
    elif boardValues.get("2,0") == playerLetter and boardValues.get("2,1") == playerLetter and boardValues.get("2,2") == playerLetter:
        print("Congratulations! You won in", playerMoves, "moves.")
    elif boardValues.get("0,0") == playerLetter and boardValues.get("1,1") == playerLetter and boardValues.get("2,2") == playerLetter:
        print("Congratulations! You won in", playerMoves, "moves.")
    elif boardValues.get("2,0") == playerLetter and boardValues.get("1,1") == playerLetter and boardValues.get("0,2") == playerLetter:
        print("Congratulations! You won in", playerMoves, "moves.")
    else:
        computer_move()

"""
checks all possible 3 in a row combinations to see if the computer has won.
"""
def check_computer_win():
    if boardValues.get("0,0") == computerLetter and boardValues.get("1,0") == computerLetter and boardValues.get("2,0") == computerLetter:
        print("You lose! The computer won in", computerMoves, "moves.")
    elif boardValues.get("0,1") == computerLetter and boardValues.get("1,1") == computerLetter and boardValues.get("2,1") == computerLetter:
        print("You lose! The computer won in", computerMoves, "moves.")
    elif boardValues.get("0,2") == computerLetter and boardValues.get("1,2") == computerLetter and boardValues.get("2,2") == computerLetter:
        print("You lose! The computer won in", computerMoves, "moves.")
    elif boardValues.get("0,0") == computerLetter and boardValues.get("0,1") == computerLetter and boardValues.get("0,2") == computerLetter:
        print("You lose! The computer won in", computerMoves, "moves.")
    elif boardValues.get("1,0") == computerLetter and boardValues.get("1,1") == computerLetter and boardValues.get("1,2") == computerLetter:
        print("You lose! The computer won in", computerMoves, "moves.")
    elif boardValues.get("2,0") == computerLetter and boardValues.get("2,1") == computerLetter and boardValues.get("2,2") == computerLetter:
        print("You lose! The computer won in", computerMoves, "moves.")
    elif boardValues.get("0,0") == computerLetter and boardValues.get("1,1") == computerLetter and boardValues.get("2,2") == computerLetter:
        print("You lose! The computer won in", computerMoves, "moves.")
    elif boardValues.get("2,0") == computerLetter and boardValues.get("1,1") == computerLetter and boardValues.get("0,2") == computerLetter:
        print("You lose! The computer won in", computerMoves, "moves.")
    else:
        player_move()

"""
Checks that there empty spaces on the board, if none can be found will declare the game is a draw.
"""
def check_for_remaining_spaces():
    global isDraw
    if boardValues.get("0,0") == "_":
        isDraw = False
    elif boardValues.get("1,0") == "_":
        isDraw = False
    elif boardValues.get("2,0") == "_":
        isDraw = False
    elif boardValues.get("0,1") == "_":
        isDraw = False
    elif boardValues.get("1,1") == "_":
        isDraw = False
    elif boardValues.get("2,1") == "_":
        isDraw = False
    elif boardValues.get("0,2") == "_":
        isDraw = False
    elif boardValues.get("1,2") == "_":
        isDraw = False
    elif boardValues.get("2,2") == "_":
        isDraw = False
    else:
        isDraw = True


def update_board(): # Prints the board with updated values
    print(boardValues.get("0,2"), boardValues.get("1,2"), boardValues.get("2,2"))
    print(boardValues.get("0,1"), boardValues.get("1,1"), boardValues.get("2,1"))
    print(boardValues.get("0,0"), boardValues.get("1,0"), boardValues.get("2,0"))


update_board()
player_move()
