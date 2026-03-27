"""Split a linked list into two alternating lists."""


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
    
class Context(object):
    """Container for two split linked lists.
    
    Attributes:
        first: The head of the first list (odd positions).
        second: The head of the second list (even positions).
    """
    
    def __init__(self, first, second):
        """Initialize Context with two split lists."""
        self.first = first
        self.second = second
    
def alternating_split(head):
    """Split a linked list into two alternating lists.
    
    Args:
        head: The head node of the linked list to split.
    
    Returns:
        Context object containing the two alternating lists.
    
    Raises:
        ValueError: If head is None or has only one node.
    """
    if head is None or head.next is None:
        raise ValueError

    first = head
    second = head.next

    current1 = first
    current2 = second

    while current1 is not None and current2 is not None and current2.next is not None:
        current1.next = current2.next
        current1 = current1.next

        current2.next = current1.next
        current2 = current2.next

    current1.next = None
    if current2 is not None:
        current2.next = None

    return Context(first, second)
