class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise IndexError

    current = node
    current_index = 0

    while current is not None:
        if current_index == index:
            return current

        current = current.next
        current_index += 1

    raise IndexError("Index out of range")
