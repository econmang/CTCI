import sys
import numpy as np

def most_common_substr(test_str1, test_str2):
    str1_len = len(test_str1)
    str2_len = len(test_str2)
    word_check = np.zeros((str1_len, str2_len), dtype=int)
    for i in range(0, str1_len):
        for j in range(0, str2_len):
            if test_str1[i] == test_str2[j]:
                if i == 0 or j == 0:
                    word_check[i][j] = 1
                else:
                    word_check[i][j] = word_check[i-1][j-1] + 1
    print(word_check)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Usage: Requires Filename")
    fName = sys.argv[1]
    with open(fName, 'r') as f:
        for line in f.readlines():
            line = line.replace('\n','')
            args = line.split(',')
            print(most_common_substr(args[0], args[1]))
