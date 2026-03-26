"""Move a node from one linked list to another."""


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
    
class Context(object):
    """Container for source and destination linked list heads.
    
    Attributes:
        source: The head node of the source linked list.
        dest: The head node of the destination linked list.
    """
    
    def __init__(self, source, dest):
        """Initialize Context with source and destination lists."""
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    """Move the first node from source list to the beginning of dest list.
    
    Args:
        source: The head node of the source linked list.
        dest: The head node of the destination linked list.
    
    Returns:
        Context object containing the updated source and dest lists.
    
    Raises:
        ValueError: If source is None.
    """
    if source is None:
        raise ValueError
    
    node_to_move = source
    source = source.next
    node_to_move.next = dest
    dest = node_to_move

    return Context(source, dest)

    




