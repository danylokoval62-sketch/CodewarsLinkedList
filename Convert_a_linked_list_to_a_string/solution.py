"""Convert a linked list to its string representation."""


def stringify(node):
    """Convert a linked list to a string representation.
    
    Args:
        node: The head node of the linked list to convert.
    
    Returns:
        String representation of the linked list in format "1 -> 2 -> 3 -> None".
    """
    result = ""
    current = node

    while current:
        result += str(current.data) + " -> "
        current = current.next

    result += "None"
    return result
