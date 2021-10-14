# Method-2 memonisation

def climbStairs(n, memo = {}):
    if n in memo:
        return memo[n]
    if n < 0:
        return 0
    if n == 0:
        return 1
    memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
    return memo[n]

# Time Complexity : O(n)
# Space Complexity : O(n)