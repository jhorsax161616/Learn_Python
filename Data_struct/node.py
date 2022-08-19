class Node():
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

head = None

""" for i in range(1, 8):
    head = Node(i, head)

while head != None:
    print(head.data)
    head = head.next """