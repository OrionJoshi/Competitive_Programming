# Method-1 Using Memoization approach

def uniquePaths(m, n, memo={}):
    key = str(m) + ',' + str(n)
    
    if key in memo:
        return memo[key]
    if m == 1  and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
        
    memo[key] =  uniquePaths(m - 1, n, memo) + uniquePaths(m, n - 1, memo)
    
    return memo[key]

# Time Complexity : O(m * n)
# Space Complexity : O(n + m)

# Input: m = 3, n = 7
# Output: 28