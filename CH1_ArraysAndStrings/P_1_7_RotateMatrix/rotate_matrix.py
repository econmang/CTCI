# Take an N x N matrix and rotate it 90 degrees

import sys
import numpy as np

try:
    fileName = sys.argv[1]
    file = open(fileName)
    i = 0
    lineArr = []
    for line in file:
        lineArr.append([int(x) for x in line.replace("\n","").split(",")])
    file.close()
    fileArr = np.matrix(lineArr)
    print("-----ORIGINAL MATRIX-----")
    print(fileArr)
    testArr = np.rot90(fileArr, 0)
    n = fileArr.shape[0]
    for x in range(0, n // 2):
        for y in range(x, n - x - 1):
            temp = fileArr[x,y]

            fileArr[x,y] = fileArr[y,n-1-x]

            fileArr[y,n-1-x] = fileArr[n-1-x,n-1-y]

            fileArr[n-1-x,n-1-y] = fileArr[n-1-y,x]

            fileArr[n-1-y,x] = temp

    print("-----ROTATED MATRIX-----")
    print(fileArr)
    print("-----TEST AGAINST MATRIX-----")
    print(testArr)
except:
    print("No file provided")
