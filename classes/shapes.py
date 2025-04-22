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
    def __init__(self, x = 5, y = 0):
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

    def convert_to_positions(self):
        pos = []

        for y, row in enumerate(self.shape): #i = index row = line
            row = list(row) #turn string to the list
            for x, column in enumerate(row):
                if row == '0':
                    pos.append(self.x+ x, self.y + y)
        
        for i, position in pos:
            pos[i] = (position[0] - 2, position[1] - 4) #2 left and 4 up (offset)

        return position
    



