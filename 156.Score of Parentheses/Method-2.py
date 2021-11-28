# Method-2 Using Stack

def scoreOfParentheses(s):
    stack = [0]
    
    for x in s:
        if x == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)
            
    return stack[-1]

# Time Complexity : O(n)
# Space Complexity : O(n)