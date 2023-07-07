import sys
import numpy as np

def most_common_substr(test_str1, test_str2):
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Usage: Requires Filename")
    fName = sys.argv[1]
    with open(fName, 'r') as f:
        for line in f.readlines():
            line = line.replace('\n','')
            args = line.split(',')
            print(most_common_substr(args[0], args[1]))
