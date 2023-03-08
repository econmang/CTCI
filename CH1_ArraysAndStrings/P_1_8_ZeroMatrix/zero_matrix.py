import sys
import numpy as np

#Where a zero is found in the matrix, zero out the entire row and column
if __name__ == "__main__":
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
        m = fileArr.shape[0]
        n = fileArr.shape[1]
        for i in range(0,m):
            for j in range(0,n):
                if fileArr[i,j] == 0:
                    fileArr[i] = np.zeros((1,n), dtype=int) 
                    fileArr[:,j] = np.zeros((m,1), dtype=int)
        print("-----ZEROED MATRIX-----")
        print(fileArr)
    except:
        print("No file provided")
