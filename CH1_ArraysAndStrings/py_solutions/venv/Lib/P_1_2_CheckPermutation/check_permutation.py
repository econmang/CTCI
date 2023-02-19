import sys

def check_perm(check_str: str, compare_str: str)-> bool:
    list_str = sorted(check_str)
    cmp_list_str = sorted(compare_str)

    if list_str == cmp_list_str:
        return True
    return False

if __name__ == "__main__":
    try:
        fileName = sys.argv[1]
        file = open(fileName)
        for line in file:
            line = line.replace("\n","")
            print(check_perm(line, "totapo"))
        file.close()

    except:
        print("File not supplied")
