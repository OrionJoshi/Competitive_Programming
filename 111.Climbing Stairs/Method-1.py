# Method-1 Using DP

def climbStairs(n):
    first = 1
    second = 1
    
    for i in range(n - 1):
        temp = first + second
        first = second
        second = temp
        
    return second

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: n = 2
# Output: 2
# Explanation: There are two ways 
# to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
