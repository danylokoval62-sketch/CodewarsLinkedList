"""Linked list operations: push and build functions."""


class Node:
    """A node in a singly linked list.
    
    Attributes:
        data: The value stored in the node.
        next: Reference to the next node (initially None).
    """
    
    def __init__(self, data):
        """Initialize a new Node with data."""
        self.data = data
        self.next = None

def push(head, data):
    """Insert a new node with data at the beginning of the linked list.
    
    Args:
        head: The current head node of the list.
        data: The value to insert.
    
    Returns:
        The new head node.
    """
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """Build and return a linked list containing nodes with values 1, 2, 3.
    
    Returns:
        The head node of the linked list [1 -> 2 -> 3 -> None].
    """
    chained = None

    for i in range(3, 0, -1):
        chained = push(chained, i)

    return chained
