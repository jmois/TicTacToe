from enum import Enum

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

NONE = 0
X = 1
O = 2

MAX_ROWS = len(board)
MAX_COLUMNS = len(board[0])


def getBoard():
    return str(board)


def placeMove(strRow, strColumn, strPiece):

    row = int(strRow)
    column = int(strColumn)
    piece = int(strPiece)

    if row >= MAX_ROWS or row < 0:
        raise Exception("Illegal row")
    if column >= MAX_COLUMNS or column < 0:
        raise Exception("Illegal column")
    if piece != X and piece != O:
        raise Exception("Piece not valid")
    if board[row][column] != NONE:
        raise Exception("There is a piece in there already")
    board[row][column] = piece
    # Check there is a winner ?

