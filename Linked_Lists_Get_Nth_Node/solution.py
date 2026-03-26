"""Get the nth node from a linked list."""


class Node(object):
    """A node in a singly linked list.
    
    Attributes:
        data: The value stored in the node.
        next: Reference to the next node (or None if last node).
    """
    
    def __init__(self, data, next=None):
        """Initialize a new Node with data and optional next reference."""
        self.data = data
        self.next = next

def get_nth(node, index):
    """Get the node at the specified index in the linked list.
    
    Args:
        node: The head node of the linked list.
        index: The zero-based index of the node to retrieve.
    
    Returns:
        The node at the specified index.
    
    Raises:
        IndexError: If node is None, index is negative, or index is out of range.
    """
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
