# Method-1 using pointer

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Time Complexity : O(n)
# Space Complexity : O(1)