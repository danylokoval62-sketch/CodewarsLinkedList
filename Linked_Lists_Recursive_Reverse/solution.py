"""Recursively reverse a linked list."""


class Node(object):
    """A node in a singly linked list.
    
    Attributes:
        data: The value stored in the node.
        next: Reference to the next node (initially None).
    """
    
    def __init__(self, data=None):
        """Initialize a new Node with optional data."""
        self.data = data
        self.next = None

def reverse(head):
    """Reverse a linked list recursively.
    
    Args:
        head: The head node of the linked list to reverse.
    
    Returns:
        The head node of the reversed linked list.
    """
    if head is None or head.next is None:
        return head

    new_node = reverse(head.next)
    head.next.next = head
    head.next = None

    return new_node
