# Method-1

def deleteDuplicates(head):
    if not head or not head.next:
        return head

    temp = ListNode(0,head)
    cur = head
    pre = temp
    
    while cur and cur.next:
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        if pre.next == cur:
            pre = pre.next
            
        else:
            pre.next = cur.next
            
        cur = cur.next

    return temp.next

# Time Complexity : O(n)
# Space Complexity : O(1)