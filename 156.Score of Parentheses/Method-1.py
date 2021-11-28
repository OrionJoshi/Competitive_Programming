# Method-1

def scoreOfParentheses(s):
    balance = 0
    result = 0
    
    for i, x in enumerate(s):
        if x == '(':
            balance += 1
        else:
            balance -= 1
            if s[i - 1] == '(':
                result += 2 ** balance
                
    return result

# Time Complexity : O(n)
# Space Complexity : O(1)