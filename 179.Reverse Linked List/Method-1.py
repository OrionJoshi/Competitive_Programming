# Method-1 Pointers

def reverseList(head):
    p1, p2 = None, head
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1

# Time Complexity : O(n)
# Space Complexity : O(1)