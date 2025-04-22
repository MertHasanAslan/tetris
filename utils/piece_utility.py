import random
from config.shapes_config import pieces

#return a random piece (a piece have a shape and color)
def random_piece():
    piece_name = random.choice(list(pieces.keys()))
    return pieces[piece_name]

#return shape of piece
def get_piece_shape(piece):
    return piece["shape"]

#return color of piece
def get_piece_color(piece):
    return piece["color"]

#return name of a piece
def get_piece_name(piece):
    return piece["name"]
