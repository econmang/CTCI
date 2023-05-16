from typing import Optional

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

class StackWMin:
    def __init__(self):
        self.stack: Stack = Stack()
        self.min: Stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if item <= self.min.peek() or self.min.is_empty():
            self.min.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.min.peek():
            self.min.pop()
        return item
