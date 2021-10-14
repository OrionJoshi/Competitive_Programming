# Method-3 Recursion

def climbStairs(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return climbStairs(n - 1) + climbStairs(n - 2)


# Time Complexity : O(2 ^ n)
# Space Complexity : O(n)