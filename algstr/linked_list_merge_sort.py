from linked_list import LinkedList

linked_list = LinkedList()

def merge_sort(linked_list):
    if linked_list.size() <= 1:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)


def split(linked_list):
    mid = linked_list.size() //2 -1
    mid_node = linked_list.node_at_index(mid)
    
    left_half = linked_list
    right_half = LinkedList()
    right_half.__head = mid_node.next_node
    mid_node.next_node = None
    
    return left_half, right_half
    

def merge(left, right):
    pass