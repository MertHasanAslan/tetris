

from config.shapes_config import pieces
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

class piece():
    def __init__(self, x, y, shape, shape_name, shape_color):
        self.x = x
        self.y = y
        self.shape = shape
        self.name = shape_name
        self.color = shape_color
        self.rotation = 0

    #This function will return current form of piece
    def get_current(self):
        return self.shape[self.rotation]
    
    #This function will rotate the piece
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)


    


