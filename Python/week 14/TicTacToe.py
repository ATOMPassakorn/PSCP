"""TicTacToe"""
def xo():
    """TicTacToe"""
    line1=input()
    line2=input()
    line3=input()
    board=[list(line1),list(line2),list(line3)]
    result=winner(board)
    if result:
        print(f"{result} WIN")
    else:
        print("DRAW")
def winner(board):
    """winner"""
    win=[]
    for row in board:
        if row[0] == row[1] == row[2] and row[0]!="-":
            win=row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]!="-":
            win=board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]!="-":
        win=board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]!="-":
        win=board[0][2]
    return win
xo()
