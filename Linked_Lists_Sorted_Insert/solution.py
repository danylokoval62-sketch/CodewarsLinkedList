"""Insert a node into a sorted linked list maintaining order."""


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

def sorted_insert(head, data):
    """Insert a new node with data into a sorted linked list.
    
    Args:
        head: The head node of the sorted linked list.
        data: The value to insert while maintaining sorted order.
    
    Returns:
        The head node of the updated linked list.
    """
    new_node = Node(data)

    if head is None or data < head.data:
        new_node.next = head
        return new_node

    current = head

    if current.next is not None:
        while current.next is not None and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    return head
