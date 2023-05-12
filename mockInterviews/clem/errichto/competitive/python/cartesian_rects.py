'''
 Write a function that takes in a list of Cartesian coordinates (x, y) and returns the number of rectangles formed by these coordinates.

 The initial case should only handle rectangles formed parallel to the x and y axes.
'''

class CartesianCoord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def num_rects_formed(cartesian_coords):
    for coord in cartesian_coords:
        print('(', coord.x, ',', coord.y,')')

if __name__ == '__main__':
    cartesian_coords = [CartesianCoord(0, 0), CartesianCoord(0, 1), CartesianCoord(1, 0), CartesianCoord(1, 1)]
    num_rects_formed(cartesian_coords)
