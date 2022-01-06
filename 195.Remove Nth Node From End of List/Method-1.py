# Method - 1

def removeNthFromEnd(head, n):
    fast = slow = head
    
    for _ in range(n):
        fast  = fast.next
    if not fast:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next
    return head

# Time Complexity : O(n)
# Space Complexity : O(1)