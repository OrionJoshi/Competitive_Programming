# Method-1

def swapPairs(head):
    if not head or not head.next:
        return head
    
    nextPtr = head.next
    head.next = swapPairs(nextPtr.next)
    nextPtr.next = head
    
    return nextPtr

# Time Complexity : O(n)
# Space Complexity : O(n)