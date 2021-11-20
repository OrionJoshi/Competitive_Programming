# Method-1 

def removeOuterParentheses(s):
    result = ''
    j = 0
    balance = 0
    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        elif s[i] == ')':
            balance -= 1
            
        if balance == 0:
            result = result + s[j + 1: i]
            j = i + 1
    return result

# Time Complexity : O(n)
# Space Complexity : O(n)