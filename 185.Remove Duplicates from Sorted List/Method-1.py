# Method-1

def deleteDuplicates(head):
    temp = head

    if temp == None:
        return temp

    while temp.next != None:
        if temp.val == temp.next.val:
            dup = temp.next
            temp.next = temp.next.next
            dup.next = None
        else:
            temp = temp.next

    return head

# Time Complexity : O(N)
# Space Complexity : O(1)