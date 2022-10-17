# TicTacToe
#
#  x | 0 | x
#  x | x | 0
#  x | 0 | 0


## Variables that are used througout the code
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
position = 0

## Function declaration/definitions (def)
# print hello/intro statement
def print_welcome():
    print()
    print("Welcome to the awesome tictactoe game written in python!")
    print()

# TODO: maybe we can use a loop here as well?
def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n'
          + board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n'
          + board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n')


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

def get_user_input():
    global position
    print("Player 1: Place your symbol on an empty space on the board.")
    position = input("Use a number between 1 and 9: ")


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


def is_win_vertical(current_player):
    if board[0] == current_player and board[3] == current_player and board[6] == current_player:
        return True
    elif board[1] == current_player and board[4] == current_player and board[7] == current_player:
        return True
    elif board[2] == current_player and board[5] == current_player and board[8] == current_player:
        return True
    else:
        return False

def is_win_diagonal(current_player):
    if board[0] == current_player and board[4] == current_player and board[8] == current_player:
        return True
    elif board[6] == current_player and board[4] == current_player and board[2] == current_player:
        return True
    else:
        return False


def is_win(current_player):
    if is_win_horizontal(current_player) or is_win_vertical(current_player) or is_win_diagonal(current_player):
        # TODO: not the best place, better use dedicated function for it -> refactoring!
        print("Player " + current_player + " has won!")
        return True
    else:
        return False


# TODO:
def is_tie():
    pass


## Function calls / actions

current_player = 'X'
print_welcome()
print_board()
# player 1 starts by placing his token on the board
# player 1 places the 'X' symbol
game_over = False
# while game_over == False:
# Loop until one player has won or there is a tie
while not game_over:
    # use loop to enable player to place token again if space is taken
    while True:
        get_user_input()
        if is_valid_input():   # returns True or False
            # place_token_on_board(switch_player('X'))
            place_token_on_board(current_player)
            print_board()
            break

    # -> now its player 2's turn:
    game_over = is_win(current_player)
    current_player = switch_player(current_player)

    # checks for win or tie -> game_over = True
    # check for win after every turn (starting with player 1)
    # check for tie after every turn (starting with player 1)


# print board one last time with apropriate message
# ask user if it wants to play again

