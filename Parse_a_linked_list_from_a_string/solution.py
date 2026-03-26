"""Parse a linked list from a string representation into a linked list data structure."""


class Node:
    """A node in a singly linked list.
    
    Attributes:
        data: The value stored in the node.
        next: Reference to the next node (or None if last node).
    """
    
    def __init__(self, data, next=None): 
        """Initialize a new Node with data and optional next reference."""
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """Parse a string representation of a linked list into a linked list.
    
    Args:
        list_repr: String in format "1 -> 2 -> 3 -> None"
    
    Returns:
        The head node of the created linked list, or None if empty.
    """
    copy_list = list_repr.split(" -> ")
    copy_list.pop()
    
    next_node = None
    
    for i in range(len(copy_list) - 1, -1, -1):
        current_number = int(copy_list[i])
        new_node = Node(current_number, next_node)
        next_node = new_node
        
    return next_node
