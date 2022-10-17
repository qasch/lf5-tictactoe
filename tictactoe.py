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

def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n'
          + board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n'
          + board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n')


def check_if_spot_is_occupied():
   if board[position - 1] != '-':
       print("Spot is already taken, please choose another one.")
        # new input
        return True

def place_token_on_board():
    # translate user input to list index
    # and update board / save state
    board[position - 1] = 'X'


# board = ["-", "-", "X", "-", "-", "-", "-", "-", "-"]

def check_user_input():
    # TODO: all checks implemented?
    # use global variable postition so that we can
    # change its value from inside the function
    global position
    if position.isdigit():
        position = int(position)
        # check if position is between 1 (inclusive) and 10 (exclusive)
        if position in range(1, 10):
            check_if_spot_is_occupied()
            place_token_on_board()
        else:
            print("Please enter a number between 1 and 9.")
    else:
        print("Please enter a number between 1 and 9.")

def get_user_input():
    global position
    print("Player 1: Place your symbol on an empty space on the board.")
    position = input("Use a number between 1 and 9: ")


## Function calls / actions
print_welcome()
print_board()
# player 1 starts by placing his token on the board
# player 1 places the 'X' symbol
while ________:
    get_user_input()
    check_user_input()
    print_board()

# now its player 2's turn:
# place token
# check if space is already taken
# notify user if so
# use loop to enable player to place token again if space is taken
# save state
# print board
# NOTE: use some kind of loop!
# check for win after every turn (starting with player 1)
# check for tie after every turn (starting with player 1)
# Loop until one player has won or there is a tie
# print board one last time with apropriate message
# ask user if it wants to play again

