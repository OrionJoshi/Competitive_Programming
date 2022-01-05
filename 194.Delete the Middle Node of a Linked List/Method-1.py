# Method-1

def deleteMiddle(head):
    length = 0
    temp = head
    i = 0
    
    while temp.next != None:
        length += 1
        temp = temp.next
    
    if length == 0:
        return None
    
    temp = head   
    removePos = (length // 2)
    
    if not length % 2:
        removePos -= 1 
        
    while i != removePos:
        temp = temp.next
        i += 1
        
    removeNode = temp.next
    temp.next = temp.next.next
    removeNode.next = None
    
    return head

# Time Complexity : O(n)
# Space Complexity : O(1)