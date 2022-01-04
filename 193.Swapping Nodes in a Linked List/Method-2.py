# Method-2 Using pointer

def swapNodes(head, k):
    length = 1
    temp = head
    ptr1 = head
    ptr2 = head 
    k1 = 1
    k2 = 1
    
    while temp.next != None:
        temp = temp.next
        length += 1
    while k1 != k or k2 != length + 1 -k:
        if k1 != k and k2 != length + 1 - k:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            k1 += 1
            k2 += 1
        elif k1 == k and k2 == length + 1 - k:
            break
        elif k2 != length + 1 - k:
            ptr2 = ptr2.next
            k2 += 1
        else:
            ptr1 = ptr1.next
            k1 += 1
    ptr1.val, ptr2.val = ptr2.val, ptr1.val

    return head

# Time Complexity : O(n)
# Space Complexity : O(1)