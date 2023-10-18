"""
This is the main driver and will handle user input and displaying the game
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE = HEIGHT // DIMENSION
MAX_FPS = 15    
IMAGES = {}

"""
Making global dictionary of images that will be called once
"""
def load_Images():
    pieces = ['wp', 'bp', 'wR', 'bR', 'wN', 'bN', 'wB', 'bB', 'wQ', 'bQ', 'wK', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("img/" + pieces + ".png"), (SQUARE, SQUARE))
    #We can access img with 'IMAGES[]'

"""
Main driver will handle user input and updating graphics
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = ChessEngine.GameState()
    print(gs.board) 


if __name__== "__main__":
    main()



