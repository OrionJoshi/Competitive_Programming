# Method-1 Using turtle 🐢 and hare 🐇 method

def hasCycle(head):
    if  not head:
        return False
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

# Time Complexity : O(n)
# Space Complexity : O(1)