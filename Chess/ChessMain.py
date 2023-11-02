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
        IMAGES[piece] = p.transform.scale(p.image.load("img/" + piece + ".png"), (SQUARE, SQUARE))
    #We can access img with 'IMAGES[]'

"""Graphics of whats on the board"""
def draw_Game_State(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


"""
Main driver will handle user input and updating graphics
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = ChessEngine.GameState()
    load_Images()
    running = True
    SQUARESelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                    
        draw_Game_State(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


"""Draws the Squares"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("brown")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQUARE, r*SQUARE, SQUARE, SQUARE ))



"""Draws Pieces on the board"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p .Rect(c*SQUARE, r*SQUARE, SQUARE, SQUARE))


if __name__== "__main__":
    main()



