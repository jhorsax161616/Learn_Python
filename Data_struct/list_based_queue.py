
class ListQueue:
    def __init__(self) -> None:
        self.items: list = []
        self.size: int = 0
    
    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

        return self.items[0]
    
    def dequeue(self):
        data = self.items.pop()
        self.size -= 1

        return f'{data} has been removed'

    def traverse(self):
        total_items = self.size

        for item in range(total_items):
            print(self.items[item])


food = ListQueue()

print(food.enqueue('pear'))
print(food.enqueue('banana'))
print(food.enqueue('patatas'))

food.traverse()
print(food.dequeue())
food.traverse()
