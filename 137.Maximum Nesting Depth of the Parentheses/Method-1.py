# Method-1 Using Stack

def maxDepth(s):
    length = len(s)
    count = 0
    stack = []
    
    for i in range(length):
        if s[i] == '(':
            stack.append('(')
            stackLen = len(stack)
            if count < stackLen:
                count = stackLen
        elif s[i] == ')':
            stack.pop()
    return count

# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside 
# of 3 nested parentheses in the string.