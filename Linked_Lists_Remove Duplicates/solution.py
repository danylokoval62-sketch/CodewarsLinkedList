"""Remove duplicate values from a sorted linked list."""


class Node(object):
    """A node in a singly linked list.
    
    Attributes:
        data: The value stored in the node.
        next: Reference to the next node (initially None).
    """
    
    def __init__(self, data):
        """Initialize a new Node with data."""
        self.data = data
        self.next = None

def remove_duplicates(head):
    """Remove consecutive duplicate values from a linked list.
    
    Args:
        head: The head node of the linked list.
    
    Returns:
        The head node of the linked list with duplicates removed.
    """
    if head is None:
        return None

    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next

        else:
            current = current.next

    return head
