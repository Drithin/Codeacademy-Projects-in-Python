board = []

for i in range(0,5):
    value = ["O"]*5
    board.append(value)

def print_board(board):
    for i in board:
        print " ".join(i)



print_board(board)