# Method-1

def getDecimalValue(head):
    num = head.val
    
    while head.next:
        num = num * 2 + head.next.val
        head = head.next
    return num

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10