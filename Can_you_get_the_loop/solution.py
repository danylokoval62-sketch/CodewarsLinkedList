"""Detect and measure the size of a loop in a linked list."""


def loop_size(node):
    """Find the size of a loop in a linked list using Floyd's cycle detection.
    
    Args:
        node: A node from the linked list that contains a loop.
    
    Returns:
        The size (number of nodes) in the loop.
    """
    current1 = node
    current2 = node
    count = 0

    current1 = current1.next
    current2 = current2.next.next

    while current1 != current2:
        current1 = current1.next
        current2 = current2.next.next

    current2 = current1.next
    count = 1

    while current1 != current2:
        count += 1
        current2 = current2.next

    return count
