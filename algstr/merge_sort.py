def merge_sort(list):
    if len(list) <= 1:
        return list
    
    left, right = split(list)
    left_list = merge_sort(left)
    right_list = merge_sort(right)
    
    return merge(left_list, right_list)
    
def split(list):
    mid = len(list) // 2
    
    left = list[:mid]
    right = list[mid:]
    
    return left, right


def merge(left, right):
    l = 0
    r = 0
    new_list = []
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            new_list.append(left[l])
            l += 1
        else:
            new_list.append(right[r])
            r += 1
        
    while l < len(left):
        new_list.append(left[l])
        l += 1
    
    while r < len(right):
        new_list.append(right[r])
        r += 1
    
    return new_list


def verify_sorted(list):
    if len(list) <= 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])


ml = [321, 32, 78, 462, 421, 54, 65, 54736]
print(merge_sort(ml))
print(verify_sorted(ml))
print(verify_sorted(merge_sort(ml)))