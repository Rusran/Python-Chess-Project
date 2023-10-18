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

        self.whiteToMove = True
        self.moveLog = []