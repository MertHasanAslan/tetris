import random
from config.shapes_config import pieces
from utils.piece_utility import *
"""
This game will be original tetris-like
height = 20, width = 10

tetris symbols:
    Z_reverse - green
    Z - red
    l - cyan
    O - yellow
    L_reverse - blue
    L - orange
    T - purple
"""

class tetris_piece():
    def __init__(self, x, y):
        self.piece = random_piece()
        self.x = x
        self.y = y
        self.name = get_piece_name(self.piece)
        self.shape = get_piece_shape(self.piece)
        self.color = get_piece_color(self.piece)
        self.rotation = 0

    #This function will return current form of piece
    def get_current(self):
        return self.shape[self.rotation]
    
    #This function will rotate the piece
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)



