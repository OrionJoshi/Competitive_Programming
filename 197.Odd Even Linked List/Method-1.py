# Method-1

def oddEvenList(head):
    if head == None:
        return None
    odd = head
    even = odd.next
    evenHead = even
    
    while even and even.next != None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenHead
    return head

# Time Complexity : O(n)
# Space Complexity : O(1)