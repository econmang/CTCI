'''
You are given a matrix of arrays.
Each array represents a row of the matrix.
Each element in an array represents a pixel: 0 is white, 1 is black.

The goal is to remmove all black pixels that are not connected to the border of the matrix.

Sample Input:
[
    [1, 0, 0, 0, 0, 0]
    [0, 1, 0, 1, 1, 1]
    [0, 0, 1, 0, 1, 0]
    [1, 1, 0, 0, 1, 0]
    [1, 0, 1, 1, 0, 0]
    [1, 0, 0, 0, 0, 1]
]
'''

def isBorder(i, j, matrix):
    if i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[0]) - 1:
        return True
    return False

def inBounds(i, j, matrix):
    if i < 0 or i >= len(matrix) - 1 or j < 0 or j >= len(matrix[0]) - 1:
        return False
    return True

def dfs(i, j, matrix, border_islands):
    neighbors = [
        [i - 1, j],
        [i + 1, j],
        [i, j - 1],
        [i, j + 1]
    ]

    for [x,y] in neighbors:
        if inBounds(x, y, matrix):
            if matrix[x][y] == 1 and (x,y) not in border_islands:
                border_islands[(x,y)] = True
                dfs(x, y, matrix, border_islands)

def removeIslands(matrix):
    # 1 -> black
    # 0 -> white
    
    # Dict is keyed on coordinates represented in a tuple:
    border_islands = {}

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1 and isBorder(i, j, matrix):
                border_islands[(i,j)] = True
                dfs(i, j, matrix, border_islands)

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1 and (i,j) not in border_islands: 
                matrix[i][j] = 0

    return matrix

if __name__ == '__main__':
    print("Remove Islands Test:\n------------------")
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]

    print('\nOriginal Matrix:')
    for i in range(len(matrix)):
        print(matrix[i])

    new_matrix = removeIslands(matrix)

    print('\nNew Matrix:')
    for i in range(len(new_matrix)):
        print(new_matrix[i])
