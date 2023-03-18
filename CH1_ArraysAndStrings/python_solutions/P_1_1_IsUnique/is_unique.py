import sys

def is_unique(search_str: str)-> bool:
    str_collect = "".join(str(i) for i in list(set(search_str)))
    if len(search_str) == len(str_collect):
        return True
    return False

if __name__ == "__main__":
    try:
        fileName = sys.argv[1]
        file = open(fileName)
        for line in file:
            print(is_unique(line))
        file.close()
    except:
        print("File not supplied")
