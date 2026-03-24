def linked_list_from_string(list_repr: str) -> Node | None:
    copy_list = list_repr.split(" -> ")
    copy_list.pop()
    
    next_node = None
    
    for i in range(len(copy_list) - 1, -1, -1):
        current_number = int(copy_list[i])
        new_node = Node(current_number, next_node)
        next_node = new_node
        
    return next_node
