from typing import Any
from node import Node

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size: int = 0

    def push(self, data: Any):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size += 1

        return self.top.data

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        
        else:
            return "The stack is empty"
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        while self.top:
            self.pop()
        
        return "emptied stack"



""" food = Stack()

print(food.push('egg'))
print(food.push('ham'))
print(food.push('spam'))

print(food.pop()) # -> spam
print(food.peek()) # -> ham
print(food.clear())
print(food.peek()) """