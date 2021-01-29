def win_check(strRow, strColumn, strPiece):

    row = int(strRow)
    column = int(strColumn)
    piece = int(strPiece)

    return ((board[1][1] == piece and board[1][2] == piece and board[1][3] == piece) or
             (board[2][1] == piece and board[2][2] == piece and board[2][3] == piece) or
            (board[3][1] == piece and board[3][2] == piece and board[3][3] == piece) or
            (board[1][1] == board[2][1] == board[3][1] == piece) or
            (board[1][2] == board[2][2] == board[3][2] == piece) or
            (board[1][3] == board[2][3] == board[3][3] == piece) or
            (board[1][1] == board[2][2] == board[3][3] == piece) or
            (board[3][1] == board[2][2] == board[1][3] == piece))

    ## Return Boolean
    