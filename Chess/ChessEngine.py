"""
This class will hold the data for the current state of the game
Also will determin valid moves and move history
"""

##using 2d list to make the board. we should change this using numpy for better efficiency 
class GameState():
    def __init__(self):
        #8x8 2d list, first character is the color the second char is the peice 
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--" , "--", "--"],
            ["--", "--", "--", "--", "--", "--" , "--", "--"],
            ["--", "--", "--", "--", "--", "--" , "--", "--"],
            ["--", "--", "--", "--", "--", "--" , "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        

        self.white_To_Move = True
        self.move_Log = []   
        
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endCol][move.endCol] = move.pieceMove
        self.move_Log.append(move)
        self.white_To_Move = not self.white_To_Move
        
class Move:

    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4,
                     "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3,
                     "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, startSQUARE, endSQUARE, board): 
        self.startRow = startSQUARE[0]
        self.startCol = startSQUARE[1]
        self.endRow = endSQUARE[0]
        self.endCol = endSQUARE[1]
        self.pieceMove = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    def getRankFile(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]       