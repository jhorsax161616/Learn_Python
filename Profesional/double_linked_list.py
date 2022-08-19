class Node(object):
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
    
class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None) -> None:
        Node.__init__(self, data, next)
        self.previous = previous

head = TwoWayNode(1)
tail = head

for data in range(2, 7):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next

probe = tail

while probe != None:
    print(probe.data)
    probe = probe.previous