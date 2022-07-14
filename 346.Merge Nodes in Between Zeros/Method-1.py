# Method-1

def mergeNodes(head):
    ptr1 = head
    ptr2 = head.next
    s = 0
    
    while ptr2:
        if ptr2.val == 0:
            ptr1 = ptr1.next
            ptr1.val=s
            s=0
        else:
            s+=ptr2.val
            
        ptr2 = ptr2.next
        
    ptr1.next=None
    
    return head.next

# Time Complexity : O(n)
# Space Complexity : O(1)