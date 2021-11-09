# Method-2 Iterative

def maxDepth(s):
    maxDepth = 0
    count = 0
    
    for x in s:
        if x == '(':
            count += 1
        elif x == ')':
            if maxDepth < count:
                maxDepth = count
            count -= 1
            
    return maxDepth
    
# Time Complexity : O(n)
# Space Complexity : O(1)