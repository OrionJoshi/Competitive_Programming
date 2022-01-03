# Method-1

def mergeInBetween(list1, a, b, list2):
    i = 0
    j = 0
    ptr1 = list1
    ptr2 = list1
    
    while ptr2.next != None:
        if i + 1 != a and j != b:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            i += 1
            j += 1
        elif i + 1 == a and j == b:
            break
        elif i + 1 == a:
            ptr2 = ptr2.next
            j += 1

    temp = list2
    while temp.next != None:
        temp = temp.next
        
    ptr1.next = list2
    ptr3 = ptr2.next
    temp.next = ptr3
    ptr2.next = None
    
    return list1

# Time Complexity : O(n)
# Space Complexity : O(1)