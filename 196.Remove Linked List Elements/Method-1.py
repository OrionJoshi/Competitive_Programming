# Method-1

def removeElements(head, val):
    if head == None:
        return head   
    temp = head
    prv = None

    while temp.next != None:
        if temp.val == val and prv == None:
            head = head.next
            temp.next = None
            temp = head
        elif temp.val == val:
            temp1 = temp
            temp = temp.next
            prv.next = temp
            temp1.next = None
        else:
            prv = temp
            temp = temp.next
            
    if not temp.val == val:
        return head
    else:
        if prv:
            prv.next = None
            return head
        else:
            return None

# Time Complexity : O(n)
# Space complexity : O(1)