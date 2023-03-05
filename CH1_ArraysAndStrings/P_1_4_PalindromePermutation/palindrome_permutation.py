import sys
from itertools import permutations

def check_perm_palindrome(check_text):
    check_text = check_text.replace(" ","").strip().lower()
    perms = [''.join(p) for p in permutations(check_text) if ''.join(p)[::-1] == ''.join(p)]
    if len(perms) > 0:
        return True
    return False

if __name__ == "__main__":
    check_text = ''.join(sys.argv[1:])
    print(check_perm_palindrome(check_text))
