def print_board(board):
    print("--------------")
    for row in board:
        print(" | " + " | ".join(row) + " | ")
        print("---------------")

def check_win(board, player):
    #Check rows, columns, and diagonals for a win
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
           (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
           (board[0][2] == player and board[1][1] == player and board[2][0] == player):
            return True

def tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = ['x', 'o']
    current_player = 0
    print_board(board)
    while True:
        row = int(input("Player " + players[current_player] + ", choose a row(1-3): ")) - 1
        col = int(input("Player " + players[current_player] + ", choose a column(1-3): ")) - 1
        if board[row][col] != ' ':
           print("That space is already taken. Try again.")
           continue
        board[row][col] = players[current_player]
        print_board(board)
        if check_win(board, players[current_player]):
           print("Player " + players[current_player] + " wins! ")
           break
        if all([space != ' ' for row in board for space in row]):
           print("It's a tie!")
           break
        if check_win(board, players [current_player]):
            print("players " + players[current_player] + " play again ")
        current_player = (current_player + 1) % 2

tic_tac_toe() 
