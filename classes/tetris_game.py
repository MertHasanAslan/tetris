import pygame
from config.game_config import *
from classes.shapes import *

class tetris_game():
    def __init__(self):
        self.grid = [] #grid of game
        self.locked_pos = {} #keys = coordinates values = colors.
        self.create_grid() #create a grid when game starts.
        self.curr_piece = tetris_piece()

    def create_grid(self): 
        self.grid = [[(204, 204, 179) for x in range(col)] for y in range(row)] #make a grid for y rows and x columns with rgb (204, 204, 179)

        
        for (x, y), color in self.locked_pos.items(): #unpack x and y because items will be like [((x, y), (255, 0, 0))...]
            self.grid[y][x] = color

    def shape_to_format(self):
        return self.curr_piece.convert_to_positions()
    
    def empty_space(self):
        return None

