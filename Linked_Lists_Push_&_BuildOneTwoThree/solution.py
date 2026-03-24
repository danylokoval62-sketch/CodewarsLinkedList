class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    chained = None

    for i in range(3, 0, -1):
        chained = push(chained, i)

    return chained
