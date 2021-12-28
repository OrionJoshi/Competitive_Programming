# Method-1 Using Stack

def isPalindrome(head):
    stack = []
    temp = head
    
    while temp.next != None:
        stack.append(temp.val)
        temp = temp.next
    stack.append(temp.val)
    while head.next != None:
        currEle = stack.pop()
        
        if head.val != currEle:
            return False
        head = head.next
    return True

# Time Complexity : O(n)
# Space Complexity : O(n)