# Method-1

def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: break
    else: return None
    while head != slow:
        head, slow = head.next, slow.next
    return head

# Time Complexity : O(n)
# Space Complexity : O(1)