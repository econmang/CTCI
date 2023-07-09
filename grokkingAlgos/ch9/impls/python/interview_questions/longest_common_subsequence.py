import numpy as np
import sys

def find_lcs(S1, S2, m, n):
    word_check = np.zeros((m+1,n+1), dtype=int)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                word_check[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                word_check[i][j] = word_check[i-1][j-1] + 1
            else:
                word_check[i][j] = max(word_check[i-1][j], word_check[i][j-1])

    idx = word_check[m][n]

    lcs = [""] * (idx+1)

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs[idx-1] = S1[i-1]
            i -= 1
            j -= 1
            idx -= 1

        elif word_check[i-1][j] > word_check[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    print("S1: " + S1 + "\nS2 :" + S2)
    print("LCS: " + "".join(lcs))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Usage: Requires Filename")
    fName = sys.argv[1]
    with open(fName, 'r') as f:
        for line in f.readlines():
            line = line.replace('\n','')
            words = line.split(',')
            find_lcs(words[0], words[1],len(words[0]), len(words[1]))
