# TicTacToe
#
#  x | 0 | x
#  x | x | 0
#  x | 0 | 0

# print hello/intro statement
print("Welcome to the awesome tictactoe game written in python!")

# print board
print("""
- | - | -
- | - | -
- | - | -
""")

#  1 | 2 | 3
#  4 | 5 | 6
#  7 | 8 | 9

# index   0 , 1, 2 ...
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# player 1 starts by placing his token on the board
# player 1 places the 'X' symbol
print("Player 1: Place your symbol on an empty space on the board.")
position = input("Use a number between 1 and 9: ")

# check user input
if position.isdigit():
    position = int(position)
    # check if position is between 1 (inclusive) and 10 (exclusive)
    if position in range(1, 10):
        # translate user input to list index
        # and update board / save state
        board[position - 1] = 'X'
    else:
        print("Please enter a number between 1 and 9.")
else:
   print("Please enter a number between 1 and 9.")

# print board again
print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n'
      + board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n'
      + board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n')

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

