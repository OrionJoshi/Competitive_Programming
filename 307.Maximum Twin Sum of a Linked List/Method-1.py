# Method-1

def pairSum(head):
    slow, fast = head, head
    maxVal = 0

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    curr, prev = slow, None

    while curr:       
        curr.next, prev, curr = prev, curr, curr.next   

    while prev:
        maxVal = max(maxVal, head.val + prev.val)
        prev = prev.next
        head = head.next

    return maxVal

# Time Complexity : O(n)
# Space Complexity : O(1)