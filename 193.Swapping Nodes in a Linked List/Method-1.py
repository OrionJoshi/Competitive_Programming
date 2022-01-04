# Method-1

def swapNodes(head, k):
    lst = []
    temp = head
    
    while temp.next != None:
        lst.append(temp.val)
        temp = temp.next
    lst.append(temp.val)
    
    # Swapping
    lst[k - 1], lst[-k] = lst[-k], lst[k - 1]
    
    temp = head
    i = 0
    while temp.next != None:
        temp.val = lst[i]
        i += 1
        temp = temp.next
        
    temp.val = lst[i]
    
    return head

# Time Complexity : O(n)
# Space Complexity : O(n)