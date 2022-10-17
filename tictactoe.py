#################################################
# A simple implementation of the TicTacToe game
#
# Author: GFN-LF5
# Date: October 2022
# Version: 0.1
##################################################


## Layout of our board:
#  x | 0 | x
#  x | x | 0
#  x | 0 | 0

## Index of our board:
#  0 | 1 | 2
#  3 | 4 | 5
#  6 | 7 | 8


###
### Variables that are used througout the code
###
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
position = 0


###
### Function declaration/definitions (def)
###
def print_welcome():
    print()
    print("Welcome to our awesome tictactoe game written in python!")
    print()


# TODO: maybe we can use a loop here as well?
def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n'
          + board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n'
          + board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n')


def get_user_input():
    global position
    print("Player 1: Place your symbol on an empty space on the board.")
    position = input("Use a number between 1 and 9: ")


def is_valid_input():
    # TODO: all checks implemented?
    # use global variable postition so that we can
    # change its value from inside the function
    global position
    if position.isdigit():
        position = int(position)
        # check if position is between 1 (inclusive) and 10 (exclusive)
        if position in range(1, 10):
            if not is_spot_occupied():
                return True
        else:
            print("Please enter a number between 1 and 9.")
            return False
    else:
        print("Please enter a number between 1 and 9.")
        return False


def is_spot_occupied():
    if board[position - 1] != '-':
        # spot is taken
        print("Spot is already taken, please choose another one.")
        return True
    else:
        # spot is available
        return False


def place_token_on_board(current_player):
    # translate user input to list index
    # and update board / save state
    board[position - 1] = current_player


def switch_player(current_player):
    if current_player != 'O':
        current_player = 'O'
    else:
        current_player = 'X'
    return current_player


# TODO: Optimize code, maybe use a loop or something?
def is_win_horizontal(current_player):
   if board[0] == current_player and board[1] == current_player and board[2] == current_player:
       return True
   elif board[3] == current_player and board[4] == current_player and board[5] == current_player:
       return True
   elif board[6] == current_player and board[7] == current_player and board[8] == current_player:
       return True
   else:
       return False


# TODO: Optimize code, maybe use a loop or something?
def is_win_vertical(current_player):
    if board[0] == current_player and board[3] == current_player and board[6] == current_player:
        return True
    elif board[1] == current_player and board[4] == current_player and board[7] == current_player:
        return True
    elif board[2] == current_player and board[5] == current_player and board[8] == current_player:
        return True
    else:
        return False

# TODO: Optimize code, maybe use a loop or something?
def is_win_diagonal(current_player):
    if board[0] == current_player and board[4] == current_player and board[8] == current_player:
        return True
    elif board[6] == current_player and board[4] == current_player and board[2] == current_player:
        return True
    else:
        return False


def is_win(current_player):
    if is_win_horizontal(current_player) or is_win_vertical(current_player) or is_win_diagonal(current_player):
        # TODO: not the best place for print statement, better use a dedicated function for it -> refactoring!
        print("Player " + current_player + " has won!")
        return True
    else:
        return False


# TODO: Implementation
def is_tie():
    pass


###
### Function calls / actions
### our 'running' program
###

# player 1 starts by placing his token on the board
# player 1 places the 'X' symbol
current_player = 'X'
print_welcome()
print_board()
game_over = False
# Loop until one player has won or there is a tie
while not game_over:
    # use loop to enable player to place token again if spot is already taken
    while True:
        get_user_input()
        if is_valid_input():   # returns True or False
            place_token_on_board(current_player)
            print_board()
            break

    # we check for win (and tie) after every move of every player
    game_over = is_win(current_player)
    # now its the other player's turn:
    current_player = switch_player(current_player)


# TODO: print board one last time with apropriate message
# TODO: ask user if it wants to play again


###
### Ideas for refactoring/optimization/more functionality:
###
# - write more/better comments for what is going on in our code, why we do certain things etc.
#   + look up how functions/methods are commented in python and apply it
# - implement a computer opponent
#   + simplest form: computer puts token in a randomly generated spot
#   + improve AI (see below)
# - refactor code with TODOs found in the comments
# - get rid of global statements
#   + try to pass arguments to our functions to get same result
# - implement a very basic AI:
#   + check if there are two equal symbols from opponent in a row/column/diagonal
#      -> place token in free spot -> defence
#   + check if there are two equal symbols from computer in a row/column/diagonal
#      -> place token in free spot -> attack
# - use a two-dimensioal array for the board, like board[row][col]
#   -> should make checks simpler, closer to our way of thinking about the board etc.
# - implement the whole game object oriented (class for board, class for player etc.)
