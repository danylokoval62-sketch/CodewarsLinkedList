def stringify(node):
    result = ""
    current = node

    while current:
        result += str(current.data) + " -> "
        current = current.next

    result += "None"
    return result
