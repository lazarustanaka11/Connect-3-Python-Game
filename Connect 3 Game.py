import sys

# creating board using list
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# boolean for checking if game is still running
game_not_over = True
# winner
winner = None
# current player
current_player = "X"  # we want to always start with X


# function to desplay the board
def display_game_board():
    print("Connect 3 Game")
    print("")
    print("BOARD       ORDER SHOWN HERE")
    print(board[0] + "|" + board[1] + "|" + board[2] + "         |1|2|3|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "         |4|5|6|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "         |7|8|9|")
    print(" ")


def play():
    display_game_board()
    while game_not_over:
        get_player(current_player)
        # checking if the game is not over
        is_game_over()
        # change to give the another player a turn
        change_player()

    # jump out of while loop if the game is over
    if winner == "X" or winner == "O":
        print(winner + " HAS WON THE GAME")
    else:
        print("You tied")


def get_player(player):
    print(player + " is playing")
    try:
        place = int(input("Place your piece from 1-9 on board:")) - 1
    except:
        print("wrong input entered please restart game")
        sys.exit()

    board[place] = player
    display_game_board()


def is_game_over():
    check_win()
    check_tie()


def check_win():
    global winner
    row_connection = check_row_connection()
    collumn_connection = check_collumn_connection()
    diagonal_connection = check_diagonal_connection()

    if row_connection:
        winner = row_connection
    elif collumn_connection:
        winner = collumn_connection
    elif diagonal_connection:
        winner = diagonal_connection
    else:
        winner = None
    return


def check_row_connection():
    global game_not_over
    # checking for row connection
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_not_over = False
        # returning which player is the winner
    if row_1:
        return board[1]
    elif row_2:
        return board[4]
    elif row_3:
        return board[7]
    return


def check_collumn_connection():
    global game_not_over
    # checking for collumn connection
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_not_over = False
        # returning which player is the winner
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonal_connection():
    global game_not_over
    # checking for diagonal connection
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2:
        game_not_over = False
        # returning which player is the winner
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


def check_tie():
    global game_not_over
    if "-" not in board:  # if board is full and no winner return tie
        game_not_over = False
    return


def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play()