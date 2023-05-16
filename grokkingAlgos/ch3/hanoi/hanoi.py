# Just doing a quick implementation of the Tower of Hanoi problem to illustrate recursion.

'''
  _      |      |
 ___     |      |
_____    |      |
'''

def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        print("Move disk", n, "from", source, "to", target)
        hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    hanoi(3, "A", "C", "B")
