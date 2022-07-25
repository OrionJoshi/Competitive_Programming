# Method-1

def reverseBetween(head, left, right):
    temp = ListNode(0)
    temp.next = head

    pre = temp
    cur = temp.next

    for i in range(1,left):
        cur = cur.next
        pre = pre.next

    for i in range(right - left):
        tep = cur.next
        cur.next = tep.next
        tep.next  = pre.next
        pre.next = tep

    return temp.next

# Time Complexity : O(n)
# Space Complexity : O(n)