"""Swap adjacent node pairs in a linked list."""


class Node:
    """A node in a singly linked list.
    
    Attributes:
        next: Reference to the next node (initially None).
    """
    
    def __init__(self, next=None):
        """Initialize a new Node with optional next reference."""
        self.next = next

def swap_pairs(head):
    """Swap adjacent pairs of nodes in a linked list.
    
    Args:
        head: The head node of the linked list.
    
    Returns:
        The head node of the linked list with adjacent pairs swapped.
    """
    new_node = Node(0)
    new_node.next = head

    prev = new_node

    while prev.next and prev.next.next:

        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return new_node.next
